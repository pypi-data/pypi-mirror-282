# -*- coding: utf-8 -*-
import inspect
import logging
from asyncio import CancelledError
from collections import deque
from typing import Iterable, Optional

from pydantic import BaseModel
from pydantic_core import ValidationError

from .dispatcher import JarpcDispatcher
from .errors import JarpcError, JarpcInvalidParams, JarpcParseError, JarpcServerError
from .format import JarpcRequest, JarpcResponse, json_dumps, json_loads

logger = logging.getLogger(__name__)


def get_args_representation(args: Iterable) -> str:
    """
    ['c', 'a', 'b'] -> "a, b, c"
    {'b',"a"} -> "a, b"
    """
    return ", ".join(sorted(args))


def check_function_call(fun, kwargs: dict, context: dict) -> (bool, Optional[str]):
    """
    Check that `kwargs` match signature of `fun` given `context`.
    Positional arguments in call are not supported.

    Minimal valid argument set: positional args with no default + kw-only args with no default,
                                except for what is provided by context.
    Maximum valid argument set: all positional + all kw-only args IF no **varkw present,
                                except for what is provided by context.
    If **varkw is present, there is no upper limit.
    *varargs has no effect because there are no positional args in call.
    If fun is a method, args[0] is self. If fun is a callable object, we have to look at its __call__

    :returns (is_ok, explanation)
    """
    argspec = inspect.getfullargspec(fun)
    args_deque = deque(argspec.args)
    if inspect.ismethod(fun) or inspect.ismethod(fun.__call__):
        # skip self
        args_deque.popleft()
    allowed_args = set(args_deque)
    if argspec.defaults:
        # skip defaults
        for _ in argspec.defaults:
            args_deque.pop()
    required_args = set(args_deque)

    required = (
        (required_args | set(argspec.kwonlyargs))
        - (argspec.kwonlydefaults or {}).keys()
        - context.keys()
        - {"jarpc_request"}
    )
    if required - kwargs.keys():
        return (
            False,
            f"Missing arguments: {get_args_representation(required - kwargs.keys())}",
        )

    if argspec.varkw is None:
        allowed = (
            (allowed_args | set(argspec.kwonlyargs))
            - context.keys()
            - {"jarpc_request"}
        )
        if kwargs.keys() - allowed:
            return (
                False,
                (
                    "Unexpected arguments:"
                    f" {get_args_representation(kwargs.keys() - allowed)}"
                ),
            )
    else:
        # if **varkw is present, anything is considered allowed except for args from context
        restricted_intersection = kwargs.keys() & (context.keys() | {"jarpc_request"})
        if restricted_intersection:
            return (
                False,
                (
                    "Unavailable arguments:"
                    f" {get_args_representation(restricted_intersection)}"
                ),
            )
    return True, None


class JarpcManager:
    def __init__(
        self,
        dispatcher: JarpcDispatcher,
        context: dict = None,
        loads=json_loads,
        dumps=json_dumps,
    ):
        self.dispatcher = dispatcher
        self.context = (
            context or dict()
        )  # per-manager context cannot contain jarpc_request
        self.loads = loads
        self.dumps = dumps

    def handle(self, request: str) -> Optional[str]:
        """Handle request string, producing either response string or None if no response is required."""
        jarpc_response = self.get_response(request_string=request)
        if jarpc_response is not None:
            return jarpc_response.model_dump_json()

    def get_response(self, request_string: str) -> Optional[JarpcResponse]:
        """Returns either JarpcResponse or None if no response is required."""
        request_id = None
        rsvp = True
        try:
            try:
                request = JarpcRequest.model_validate_json(request_string)
            except ValidationError:
                raise JarpcParseError()
            if request.expired:
                logger.warning(f"Request arrived too late: {request}")
                return None

            request_id = request.id
            rsvp = request.rsvp

            method = self.dispatcher[request.method]
            try:
                result = self._call_method(method, request)
            except TypeError:
                is_call_ok, explanation = check_function_call(
                    method, request.params, self.context
                )
                if is_call_ok:
                    raise
                logger.debug(
                    f"wrong signature in call to {request.method}: {explanation}"
                )
                raise JarpcInvalidParams(explanation)

            if request.expired:
                logger.warning(f"Request took too long to complete: {request}")
                return None
            return JarpcResponse(request_id=request_id, result=result) if rsvp else None
        except JarpcError as e:
            logger.debug(e, exc_info=True)
            return (
                JarpcResponse(request_id=request_id, error=e.as_dict())
                if rsvp
                else None
            )
        except Exception as e:
            logger.exception(e)
            return (
                JarpcResponse(
                    request_id=request_id, error=JarpcServerError(e).as_dict()
                )
                if rsvp
                else None
            )

    def _call_method(self, method, request: JarpcRequest):
        # prepare params passed from manager context
        context_params = dict()
        method_sig = inspect.signature(method)
        if "jarpc_request" in method_sig.parameters:
            context_params["jarpc_request"] = request
        for param, value in self.context.items():
            if param in inspect.signature(method).parameters:
                context_params[param] = value
        # do call
        result = method(**request.params, **context_params)

        # get the expected return type from the method's type hints
        return_annotation = method_sig.return_annotation

        # if the return annotation is a pydantic model
        if return_annotation is not inspect.Signature.empty and issubclass(
            return_annotation, BaseModel
        ):
            # if result is a dict, validate and return the pydantic model
            if isinstance(result, dict):
                return return_annotation(**result)
            # if result is an instance of another class, try to convert it
            elif not isinstance(result, return_annotation):
                try:
                    return return_annotation.model_validate(
                        result, from_attributes=True
                    )
                except ValidationError as e:
                    raise JarpcParseError(
                        f"Failed to convert return value to {return_annotation}: {e}"
                    )

        # if no specific return type is expected or it is not a pydantic model, return the result as is
        return result


class AsyncJarpcManager(JarpcManager):
    async def handle(self, request: str) -> Optional[str]:
        """Handle request string, producing either response string or None if no response is required."""
        jarpc_response = await self.get_response(request_string=request)
        if jarpc_response is not None:
            return jarpc_response.model_dump_json()

    async def get_response(self, request_string: str) -> Optional[JarpcResponse]:
        """Returns either JarpcResponse or None if no response is required."""
        request_id = None
        rsvp = True
        try:
            try:
                request = JarpcRequest.model_validate_json(request_string)
            except ValidationError:
                raise JarpcParseError()
            if request.expired:
                logger.warning(f"Request arrived too late: {request}")
                return None

            request_id = request.id
            rsvp = request.rsvp

            method = self.dispatcher[request.method]
            try:
                result = await self._call_method(method, request)
            except TypeError:
                is_call_ok, explanation = check_function_call(
                    method, request.params, self.context
                )
                if is_call_ok:
                    raise
                logger.debug(
                    f"wrong signature in call to {request.method}: {explanation}"
                )
                raise JarpcInvalidParams(explanation)

            if request.expired:
                logger.warning(f"Request took too long to complete: {request}")
                return None
            return JarpcResponse(request_id=request_id, result=result) if rsvp else None
        except CancelledError:
            raise
        except JarpcError as e:
            logger.debug(e, exc_info=True)
            return (
                JarpcResponse(request_id=request_id, error=e.as_dict())
                if rsvp
                else None
            )
        except Exception as e:
            logger.exception(e)
            return (
                JarpcResponse(
                    request_id=request_id, error=JarpcServerError(e).as_dict()
                )
                if rsvp
                else None
            )

    async def _call_method(self, method, request: JarpcRequest):
        result = super()._call_method(method, request)
        # if `method` is async function, `result` is coroutine
        if inspect.isawaitable(result):
            result = await result
        return result

"""
Prasar Module Documentation

This module provides a framework for event handling in Python, supporting both synchronous and asynchronous events. 
It includes type checking and validation for event arguments and return types.

Classes:
- __Event__: Represents an individual event with its associated function and type information.
- Prasar: The main class for binding and emitting events.

Dependencies:
- inspect: Used for introspection of function signatures and parameters.
- asyncio: Handles asynchronous operations and coroutines.
- typing: Provides type hinting capabilities.
- prasar_logger: Custom logging module (implementation not shown in the provided code).

"""

import inspect
import asyncio
from typing import Any, Callable, get_type_hints
from prasar_logger import Logger

class __Event__:
    """
    Represents an individual event with its associated function and type information.
    
    This class is responsible for storing event details and performing type checking.

    Attributes:
        _name (str): The name of the event.
        _func (Callable[..., Any]): The function associated with the event.
        _args_types (tuple[Any, ...]): Expected types of the function arguments.
        _return_type (Any): Expected return type of the function.
        _is_coroutine (bool): Indicates whether the function is a coroutine.
        _logger (Logger): Logger instance for this class.

    Methods:
        __init__: Initializes the Event object.
        __verify__: Verifies the function signature and types.
        _verify_args: Verifies the arguments passed during event emission.
    """

    def __init__(self, name: str, func: Callable[..., Any], args_types: tuple[Any, ...], return_type: Any, is_coroutine: bool) -> None:
        """
        Initializes the Event object.

        Args:
            name (str): The name of the event.
            func (Callable[..., Any]): The function associated with the event.
            args_types (tuple[Any, ...]): Expected types of the function arguments.
            return_type (Any): Expected return type of the function.
            is_coroutine (bool): Indicates whether the function is a coroutine.

        Raises:
            RuntimeError: If there's a mismatch in function signature or types.
        """
        self._name = name
        self._func = func
        self._args_types = args_types
        self._return_type = return_type
        self._is_coroutine = is_coroutine
        self._logger = Logger(str(__class__)).get_logger()
        self.__verify__()

    def __verify__(self) -> None:
        """
        Verifies the function signature and types.

        This method checks:
        1. The number of arguments matches the expected count.
        2. The types of arguments match the expected types.
        3. The function is a coroutine if expected to be one, and vice versa.
        4. The return type matches the expected return type.

        Raises:
            RuntimeError: If any of the checks fail.
        """
        signature = inspect.signature(self._func)
        arg_types = get_type_hints(self._func)
        
        # Check number of arguments
        if len(signature.parameters) != len(self._args_types):
            raise RuntimeError(f"Number of arguments mismatch. Expected {len(self._args_types)}, got {len(signature.parameters)}")
        
        # Check argument types
        for param_name, expected_type in zip(signature.parameters.keys(), self._args_types):
            actual_type = arg_types.get(param_name, Any)
            
            if expected_type != actual_type:
                raise RuntimeError(f"Type mismatch for parameter '{param_name}': expected {expected_type}, got {actual_type}")
        
        # Check if the function is a coroutine when it should be (and vice versa)
        if self._is_coroutine:
            if not asyncio.iscoroutinefunction(self._func):
                raise RuntimeError(f"Function '{self._name}' is expected to be a coroutine, but it is not.")
        else:
            if asyncio.iscoroutinefunction(self._func):
                raise RuntimeError(f"Function '{self._name}' is not expected to be a coroutine, but it is.")
        
        # Check return type
        actual_return_type = arg_types.get('return', None)
        if self._return_type != Any and self._return_type != actual_return_type:
            raise RuntimeError(f"Return type mismatch: expected {self._return_type}, got {actual_return_type}")

    def _verify_args(self, *args, **kwargs):
        """
        Verifies the arguments passed during event emission.

        This method checks:
        1. The correct number of arguments is provided.
        2. All required arguments are present.
        3. The types of provided arguments match the expected types.

        Args:
            *args: Positional arguments passed to the event.
            **kwargs: Keyword arguments passed to the event.

        Raises:
            TypeError: If the arguments do not match the expected signature or types.
        """
        signature = inspect.signature(self._func)
        try:
            bound_args = signature.bind(*args, **kwargs)
            bound_args.apply_defaults()
        except TypeError as e:
            raise TypeError(f"Invalid argument count for event '{self._name}': {str(e)}")

        # Check for extra positional arguments
        if len(args) > len(self._args_types):
            raise TypeError(f"Too many positional arguments for event '{self._name}'. Expected {len(self._args_types)}, got {len(args)}")

        for param_name, param in signature.parameters.items():
            if param.kind == inspect.Parameter.VAR_KEYWORD:
                continue  # Skip **kwargs parameter
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                continue  # Skip *args parameter
            
            if param_name not in bound_args.arguments:
                raise TypeError(f"Missing required argument '{param_name}' for event '{self._name}'")
            
            arg_value = bound_args.arguments[param_name]
            expected_type = self._args_types[list(signature.parameters).index(param_name)]
            
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Argument '{param_name}' must be of type {expected_type}, got {type(arg_value)}")

class Prasar:
    """
    The main class for binding and emitting events.

    This class allows users to bind both synchronous and asynchronous events,
    and emit them when needed.

    Attributes:
        _non_async_events (dict[str, __Event__]): Dictionary of synchronous events.
        _async_events (dict[str, __Event__]): Dictionary of asynchronous events.
        _logger (Logger): Logger instance for this class.

    Methods:
        __init__: Initializes the Prasar object.
        bind_event: Binds a synchronous event.
        bind_async_event: Binds an asynchronous event.
        emit: Emits a synchronous event.
        async_emit: Emits an asynchronous event.
    """

    def __init__(self) -> None:
        """
        Initializes the Prasar object.

        Sets up empty dictionaries for storing events and initializes the logger.
        """
        self._non_async_events: dict[str, __Event__] = {}
        self._async_events: dict[str, __Event__] = {}
        self._logger = Logger(str(__class__)).get_logger()
        
    def bind_event(self, name: str, func: Callable[..., Any], *args_types: Any, return_type: Any) -> None:
        """
        Binds a synchronous event.

        Args:
            name (str): The name of the event.
            func (Callable[..., Any]): The function to be called when the event is emitted.
            *args_types: Variable length argument list of expected argument types.
            return_type (Any): Expected return type of the function.

        Note:
            This method creates an __Event__ object and stores it in _non_async_events.
        """
        self._non_async_events[name] = __Event__(name, func, args_types, return_type=return_type, is_coroutine=False)
    
    def bind_async_event(self, name: str, func: Callable[..., Any], *args_types: Any, return_type: Any) -> None:
        """
        Binds an asynchronous event.

        Args:
            name (str): The name of the event.
            func (Callable[..., Any]): The coroutine function to be called when the event is emitted.
            *args_types: Variable length argument list of expected argument types.
            return_type (Any): Expected return type of the coroutine function.

        Note:
            This method creates an __Event__ object and stores it in _async_events.
        """
        self._async_events[name] = __Event__(name, func, args_types, return_type=return_type, is_coroutine=True)

    def emit(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """
        Emits a synchronous event.

        Args:
            name (str): The name of the event to emit.
            *args: Positional arguments to pass to the event function.
            **kwargs: Keyword arguments to pass to the event function.

        Returns:
            Any: The return value of the event function.

        Raises:
            ValueError: If the event name is not found in _non_async_events.
            TypeError: If the provided arguments do not match the expected signature or types.

        Note:
            This method verifies the arguments before calling the event function.
        """
        if name not in self._non_async_events:
            raise ValueError(f"No such event: {name}")
        
        event = self._non_async_events[name]
        event._verify_args(*args, **kwargs)
        
        self._logger.info(f"Emitting event: {name}")
        return event._func(*args, **kwargs)

    async def async_emit(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """
        Emits an asynchronous event.

        Args:
            name (str): The name of the event to emit.
            *args: Positional arguments to pass to the event coroutine.
            **kwargs: Keyword arguments to pass to the event coroutine.

        Returns:
            Any: The return value of the event coroutine.

        Raises:
            ValueError: If the event name is not found in _async_events.
            TypeError: If the provided arguments do not match the expected signature or types.

        Note:
            This method verifies the arguments before calling the event coroutine.
        """
        if name not in self._async_events:
            raise ValueError(f"No such async event: {name}")
        
        event = self._async_events[name]
        event._verify_args(*args, **kwargs)
        
        self._logger.info(f"Emitting async event: {name}")
        return await event._func(*args, **kwargs)
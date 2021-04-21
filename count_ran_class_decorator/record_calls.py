from dataclasses import dataclass
from functools import update_wrapper
from functools import wraps
from typing import Any, Optional

import wrapt as wrapt


# noinspection PyPep8Naming
class record_calls_class(wrapt.ObjectProxy):
    """this decorator counts how many time passed_funtion ran"""

    def __init__(self, passed_function):
        super().__init__(passed_function)
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.__wrapped__(*args, **kwargs)


# noinspection PyPep8Naming
class calls_record_class(object):
    """this decorator counts how many time passed_funtion ran"""

    def __init__(self, passed_function):
        self.passed_function = passed_function
        self.call_count = 0
        update_wrapper(self, passed_function)

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.passed_function(*args, **kwargs)


NO_RETURN = object()


@dataclass
class Arguments(object):
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None


def record_calls(passed_func):
    """ Decorator Function, that counts calls number, and preserve passed args and kwargs"""

    @wraps(passed_func)
    def wrapper_function(*args, **kwargs):
        wrapper_function.call_count += 1
        wrapper_function.calls.append(Arguments(args, kwargs))
        wrapped_function = None
        try:
            wrapped_function = passed_func(*args, **kwargs)
        except BaseException as e:
            wrapper_function.calls[-1].exception = e
        return wrapped_function

    wrapper_function.calls = []
    wrapper_function.call_count = 0
    return wrapper_function


@record_calls
def cube(n):
    return n ** 3


cube(3)
print(cube.calls)

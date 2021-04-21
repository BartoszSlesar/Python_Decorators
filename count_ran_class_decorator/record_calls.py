from functools import update_wrapper

import wrapt as wrapt


# noinspection PyPep8Naming
class record_calls(wrapt.ObjectProxy):
    """this decorator counts how many time passed_funtion ran"""

    def __init__(self, passed_function):
        super().__init__(passed_function)
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.__wrapped__(*args, **kwargs)






# noinspection PyPep8Naming
class calls_record(object):
    """this decorator counts how many time passed_funtion ran"""

    def __init__(self, passed_function):
        self.passed_function = passed_function
        self.call_count = 0
        update_wrapper(self, passed_function)

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.passed_function(*args, **kwargs)

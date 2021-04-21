# noinspection PyPep8Naming
class record_calls(object):
    """ decorator counts how many time passed_funtion ran"""

    def __init__(self, passed_function):
        self.passed_function = passed_function
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.passed_function(*args, **kwargs)


@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")

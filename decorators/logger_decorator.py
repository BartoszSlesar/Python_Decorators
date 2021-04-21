# Simple logger decorator which logs number of times the funcion run
from functools import wraps

def my_logger(passed_func):
    import logging
    logging.basicConfig(filename=f'{passed_func.__name__}.log', level=logging.INFO)

    @wraps(passed_func)
    def wrapper(*args, **kwargs):
        logging.info(f'function executed with arg {args} and kwarg {kwargs}')
        return passed_func(*args, **kwargs)

    return wrapper



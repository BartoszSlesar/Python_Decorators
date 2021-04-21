# Decorator show how long function ran
def timer(passed_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        wrapped_func = passed_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Function {passed_function.__name__} ran in {t2} sec.")
        return wrapped_func

    return wrapper

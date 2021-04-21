from decorators.logger_decorator import my_logger


@my_logger
def display_info(name, hobby):
    print(f'your name is {name} and hobby {hobby}')


display_info("Bartosz", "Hiking")

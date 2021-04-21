from decorators.time_decorator import timer
import time

@timer
def display_info(name, hobby):
    time.sleep(2)
    print(f'your name is {name} and hobby {hobby}')


display_info("Bartosz", "Hiking")

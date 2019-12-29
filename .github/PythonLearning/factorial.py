# importing libraries
import time
import math


def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total execution time: ", func.__name__, end - begin - 1)
    return wrapper


@calculate_time  # factorial = calculate_time(factorial)
def factorial(num):
    time.sleep(1)
    print(math.factorial(num))


factorial(10)

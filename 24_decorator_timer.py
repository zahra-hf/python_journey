#A decorator that calculates the execution time of a function and displays it after the function is executed.
#Then, use this decorator for a function that creates a list from 1 to n.

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print("Execution time:", execution_time, "seconds")

        return result

    return wrapper


@timer_decorator
def create_list(n):
    return list(range(1, n + 1))


n = int(input("Enter n: "))

result = create_list(n)

print("Result:", result)
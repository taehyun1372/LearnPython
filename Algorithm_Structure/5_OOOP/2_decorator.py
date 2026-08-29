import random
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.perf_counter() - t))
        return res
    return wrapper

def my_decorator(func):
    def wrapper():
        print("Function start")
        func()
        print("Function end")

    return wrapper

@my_decorator
def hello():
    print("Hello !")

import time

def profiler(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("elapsed time {0}".format(end - start))
        return res
    return wrapper

import random

@profiler
def rand_sleep(min, max):
    time.sleep(random.randint(min, max))
    return "slept well!"

if __name__ == "__main__":
    hello()
    result = rand_sleep(3, 5)
    print(result)
import functools
import time


def exec_time(func):
    functools.wraps(func)

    def wrapper(*args):
        t1 = time.time()
        func(*args)
        end = time.time()
        return end - t1

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))

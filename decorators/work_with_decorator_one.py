from typing import Callable, Union
import functools
from time import perf_counter

Real = Union[int, float]


def deco(func: Callable) -> Callable:
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func_result = func(*args, **kwargs)
        stop_time = perf_counter() - start_time
        print("End running function with name %s as time %.6f" % (func.__name__, stop_time))
        return func_result

    return wrapper


@deco
def add(a: Real, b: Real) -> Real:
    return a + b


result = add(10, 12)
print(result)

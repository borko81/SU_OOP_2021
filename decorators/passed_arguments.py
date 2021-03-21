from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        print(end)
        return result

    return wrapper


@measure_time
def show_num(n):
    return [i for i in range(n)]


print(show_num(10))

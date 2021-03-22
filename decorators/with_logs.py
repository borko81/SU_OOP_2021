import functools
import datetime


def decorator(filename):
    def logger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                print(f"[{datetime.datetime.now()}]: Result is:  {result}", file=f)
            return result
        return wrapper
    return logger


class About:

    def __init__(self, name):
        self.name = name

    @decorator('logs.txt')
    def show_name(self):
        return self.name


names = ['One', 'Two', 'Three']

if __name__ == '__main__':
    for name in names:
        print(About(name).show_name())

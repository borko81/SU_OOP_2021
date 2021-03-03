def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operator(func, value):
    return func(value)


print(operator(inc, 100))
print(operator(dec, 100))

# return another function in main function


def is_called():
    def is_returned(name):
        print("Inside function", name)
    return is_returned


val = is_called()
val('my-func')


# smart divide
def make_smart_divide(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return "Oops"
        return func(*args, **kwargs)
    return wrapper


@make_smart_divide
def divide(a, b):
    return a / b


print(divide(10, 0))

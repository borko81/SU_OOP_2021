def multiply(times):

    def decorator(function):
        def deco(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times
        return deco

    return decorator


if __name__ == '__main__':
    @multiply(5)
    def add_ten(number):
        return number + 10


    print(add_ten(6))

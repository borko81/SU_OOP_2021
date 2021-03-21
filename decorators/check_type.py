def type_check(type):
    def decorator(function):
        def wrapper(*args):
            if isinstance(args[0], type):
                return function(*args)
            return "Bad Type"
        return wrapper
    return decorator


if __name__ == '__main__':
    @type_check(int)
    def times2(num):
        return num * 2


    print(times2(2))
    print(times2('Not A Number'))

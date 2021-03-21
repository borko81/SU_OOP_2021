def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args)}</u>"

    return wrapper


def make_italic(function):
    def wrapper(*args, **kwargs):
        return f"<i>{function(*args)}</i>"

    return wrapper


def make_bold(function):
    def wrapper(*args):
        return f"<b>{function(*args)}</b>"

    return wrapper


if __name__ == '__main__':
    @make_bold
    @make_italic
    @make_underline
    def greet(name, lastname):
        return f"Hello, {name} {lastname}"


    print(greet("Peter", "Son"))

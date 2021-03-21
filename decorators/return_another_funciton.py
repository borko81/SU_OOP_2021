def hello_func():
    def say_hi():
        return "Hi"

    return say_hi


def print_message(message):
    def inside_function():
        return message

    return inside_function


def number_increment(numbers):
    def increase():
        return map(lambda x: x + 1, numbers)

    return list(increase())


def result_to_uppercase(function):
    def inside(msg):
        result = function(msg)
        return result.upper()

    return inside


@result_to_uppercase
def show_msg(message):
    return message




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


print(number_increment([1, 2, 3]))

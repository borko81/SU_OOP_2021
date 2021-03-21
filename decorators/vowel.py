def vowel_filter(function):
    def wrapper():
        result = function()
        data = filter(lambda x: x in 'aouyie', result)
        return list(data)

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


if __name__ == '__main__':
    print(get_letters())

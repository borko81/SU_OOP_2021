class First:

    DEFAULT_PARAM = "name_with_small_letters"

    def __init__(self, name):
        self.name = name
        self.default = self.__class__.DEFAULT_PARAM

    def __repr__(self):
        return f"[{self.__class__.__name__}]: The name {self.name} has default param {self.default}"


class Second(First):
    DEFAULT_PARAM = "name_with_upper_letters"


if __name__ == "__main__":
    a1 = First("borko")
    a2 = Second("Borko")
    print(a2.__class__.__bases__[0].__name__)

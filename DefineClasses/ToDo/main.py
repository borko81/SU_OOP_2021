class Checking:
    nums: int = 0

    def __init__(self, name):
        Checking.nums += 1
        self.name = name

    def show_name(self):
        return "Hello %s " % self.name


if __name__ == '__main__':
    a1 = Checking("First")
    print(a1.show_name())
    a2 = Checking("Second")

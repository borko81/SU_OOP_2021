class Example:

    counter = 0

    def __init__(self, num: int):
        self.num = num
        print("[%d] Begin %d" % (Example.counter, self.num))

    def __call__(self):
        Example.counter += 1
        print("Special print method")


a = Example(1)
a()
b = Example(1)
        
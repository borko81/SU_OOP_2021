class reverse_iter:

    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = elements
        self.n = len(self.elements) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 0:
            result = self.elements[self.n]
            self.n -= 1
            return result
        raise StopIteration


if __name__ == '__main__':
    reversed_list = reverse_iter([1, 2, 3, 4])
    for item in reversed_list:
        print(item)

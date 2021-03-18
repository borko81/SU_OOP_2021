class countdown_iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            temp = self.count
            self.count -= 1
            if self.count < -1:
                raise StopIteration()

            return temp


class countdown_iterator2:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.count
        if self.count >= 0:
            self.count -= 1
            return temp
        raise StopIteration()


if __name__ == '__main__':
    iterator = countdown_iterator(10)
    for item in iterator:
        print(item, end=" ")

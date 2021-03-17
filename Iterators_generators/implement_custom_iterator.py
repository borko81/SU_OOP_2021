class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            result = self.start
            self.start += 1
            if self.start > self.end + 1:
                raise StopIteration
            return result


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
import time
import sys

class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            if self.n == self.count:
                raise StopIteration()
            result = self.n * self.step
            self.n += 1
            return result


# class take_skip:
#
#     def __init__(self, step, count):
#         self.count = count
#         self.step = step
#         self.r = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.r
#         if self.r < self.count:
#             self.r += 1
#             return temp * self.step
#         raise StopIteration()


if __name__ == '__main__':
    t1 = time.perf_counter()
    numbers = take_skip(10, 5)
    print(sys.getsizeof(numbers))
    for number in numbers:
        print(number)
    print(time.perf_counter() - t1)

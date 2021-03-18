# class sequence_repeat:
#     def __init__(self, seq, number):
#         self.seq = list(seq)
#         self.number = number
#         self.count = 0
#         self.item = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count == self.number:
#             raise StopIteration
#
#         temp = self.seq[self.item]
#         self.seq.append(self.seq.pop(0))
#         self.count += 1
#         return temp

class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.count = 0
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise StopIteration()

        if self.current_item == len(self.seq):
            self.current_item = 0

        temp = self.seq[self.current_item]
        self.current_item += 1
        self.count += 1
        return temp


if __name__ == '__main__':
    result = sequence_repeat('abc', 5)
    for item in result:
        print(item, end='')

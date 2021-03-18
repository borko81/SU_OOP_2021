def solution():
    def integers():
        n = 1
        while 1:
            yield n
            n += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        count = 0
        for i in seq:
            if count == n:
                return result
            result.append(i)
            count += 1

    return take, halves, integers


if __name__ == '__main__':
    take = solution()[0]
    halves = solution()[1]
    print(take(5, halves()))

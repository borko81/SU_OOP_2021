def genrange(start, end):
    for i in range(start, end + 1):
        yield i

if __name__ == '__main__':
    print(list(genrange(1, 10)))

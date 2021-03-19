def fibonacci():
    previous = 0
    current = 1
    while True:
        yield previous
        previous, current = current, current + previous


if __name__ == '__main__':
    generator = fibonacci()
    for i in range(5):
        print(next(generator))

def squares(num):
    for i in range(1, num + 1):
        return (i * i for i in range(1, num + 1))


if __name__ == '__main__':
    print(list(squares(5)))

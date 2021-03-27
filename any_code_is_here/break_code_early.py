# Exit early

try:
    for i in range(1, 10):
        for j in range(1, 10):
            temp = j + i
            if temp == 6:
                print("Found %d + %d = %d" % (i, j, temp))
                raise StopIteration
except StopIteration:
    pass

print('-' * 20)

for i in range(1, 10):
    for j in range(1, 10):
        temp = j + i
        if temp == 6:
            print("Found %d + %d = %d" % (i, j, temp))
            break
    if temp == 6:
        break
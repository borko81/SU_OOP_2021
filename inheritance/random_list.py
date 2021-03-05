import random


class RandomList(list):

    def __init__(self, *args):
        super().__init__(*args)

    def get_random_element(self):
        return random.choice(self)


if __name__ == '__main__':
    test = RandomList()
    test.append(1)
    test.append(2)
    test.insert(0, 10)
    print(test.get_random_element())

class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

if __name__ == '__main__':
    pass
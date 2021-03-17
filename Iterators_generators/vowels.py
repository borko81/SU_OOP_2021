class vowels:

    def __init__(self, name):
        self.name = name
        self.vowels = 'aeiuyo'
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):

        while 1:
            temp = self.n
            if self.n == len(self.name):
                raise StopIteration
            self.n += 1

            if self.name[temp].lower() in self.vowels:
                return self.name[temp]



if __name__ == '__main__':
    my_string = vowels('abcedifuty0o')
    for char in my_string:
        print(char)

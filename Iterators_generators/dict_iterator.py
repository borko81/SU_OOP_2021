class dictionary_iter:

    def __init__(self, obj=None):
        if obj is None:
            self.obj = {}
        else:
            self.obj = obj
        self.len_obj = 0
        self.keys = list(self.obj.keys())

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            if self.len_obj == len(self.obj):
                raise StopIteration()
            key = self.keys[self.len_obj]
            temp = (key, self.obj[key])
            self.len_obj += 1
            return temp


if __name__ == '__main__':
    result = dictionary_iter({1: "1", 2: "2"})
    for x in result:
        print(x)

class Convert:
    def __init__(self, temp=0):
        self.set_temperature(temp)

    @property
    def get_temerature(self):
        return self.__temperature

    def set_temperature(self, value):
        if not isinstance(value, float):
            raise ValueError("Must be float")
        self.__temperature = value


test = Convert(12.5)
test.set_temperature(100.0)
print(test.get_temerature)

class Base:
    def __init__(self):
        self._a = 10
        self.__c = 100

    def show_c(self):
        return self.__c


class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        super().__init__()
        print("Calling protected member of base class: ")
        print(self._a)

    def show_c(self):
        return super().show_c()


class Hidden_Attribute:
    def __init__(self, password):
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        assert len(value) > 5, "Must be at least five char long"
        self.__password = value


if __name__ == "__main__":
    proba = Hidden_Attribute("password")
    proba.password = 'Pass'
    print(proba.password)

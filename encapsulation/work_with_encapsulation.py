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


class UserProfile:

    EMAIL_SUFFIX = "@mymail.com"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = __class__.email(first_name, last_name)

    def __repr__(self) -> str:
        return "{} hase email {}".format(self.full_name, self.email)

    @classmethod
    def profile_from_string(cls, sring_data):
        first_name, last_name = sring_data.split()
        return cls(first_name, last_name)

    @staticmethod
    def email(first, last):
        return "{}-{}{}".format(first.lower(), last.lower(), __class__.EMAIL_SUFFIX)

    @property
    def full_name(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value.title()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value.title()


if __name__ == "__main__":
    user_one = UserProfile("john", "Adams")
    user_two = UserProfile.profile_from_string("first last")

    print(user_one.full_name)
    print(user_one)
    print("-" * 20)
    print(user_two)
    print(user_two.email)

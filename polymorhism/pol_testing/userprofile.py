from polymorhism.pol_testing.abc_class import Abstract


class ShowInfo:

    @staticmethod
    def show_info(name, price):
        return "[+] User: %s has sallary %d" % (name, price)


class User(Abstract):
    PRICE = 100

    def __init__(self, name, age):
        super().__init__(name, age)

    def show_name_capitalize(self):
        return self.name.title()

    def show_price(self):
        return self.__class__.PRICE


class VipUser(User, ShowInfo):
    def show_price(self):
        return self.__class__.PRICE * 10


if __name__ == '__main__':
    user = VipUser('test', 39)
    print(user.show_name_capitalize())
    print(user.show_price())
    print(user.show_info(user.name, user.show_price()))

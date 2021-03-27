from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self):
        super().__init__(cost=1.5)


if __name__ == '__main__':
    print(TV().cost)

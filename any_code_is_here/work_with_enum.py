import enum


class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3


class Colors(enum.IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3

# printing enum member as string
print("The string representation of enum member is : ", end="")
print(Animal(1))
print(Animal['cat'])

data = dict()
data[Animal.dog] = "bark"

if 2 == Colors.GREEN:
    print("Green it")
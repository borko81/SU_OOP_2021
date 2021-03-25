from typing import List, Union

my_list: List[str] = ["first", "last", "something"]

if my_list:
    result = " ".join(x for x in my_list)
    print(result)
else:
    print("The list is empty")


def show_name(name: str) -> str:
    if not name:
        return "Do not allowed empty name"
    return name.upper()


x: Union[int, float] = 9.9

if x < 1 or x > 10:
    raise ValueError("Expect number between 1 and 10 include")
else:
    print("Good")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return


check = divide(1, 10)

if check and isinstance(check, float):
    print(check)
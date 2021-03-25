from typing import Union, List, Tuple, Optional

name: str = "Philip"
age: int = 39
height_metres: Union[float, int] = 180
loves: bool = True

names: List[Union[str, int]] = ['first', 'second', 1]

movie: Tuple[str, str] = ('Avenger 1', 'Avenger 2')

Movie = Tuple[str, int]

movies: List[Movie] = [
    ('Avenger', 100),
    ('Rambo', 150)
]


def show_movies(func_movies: List[Movie]) -> str:
    for title, price in func_movies:
        print(f"Title: {title}, Price: {price}")


show_movies(movies)

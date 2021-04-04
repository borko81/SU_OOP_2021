from abc import ABC, abstractmethod

from project.survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase: int):
        self.__needs_increase = needs_increase

    def apply(survivor: Survivor):
        pass

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase += value
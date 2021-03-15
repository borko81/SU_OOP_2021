from abc import ABC, abstractmethod


class Sensors(ABC):
    @abstractmethod
    def get_sensors(self):
        pass


class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type


class Android(Robot, Sensors):
    def get_sensors(self):
        return 4


class Chappie(Robot):
    def get_sensors(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.get_sensors())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)

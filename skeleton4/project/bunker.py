from typing import List

from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: List[Survivor] = []
        self.supplies: List[Supply] = []
        self.medicine: List[Medicine] = []

    @property
    def food(self):
        temp = [s for s in self.supplies if s.__class__.__name__ == 'FoodSupply']
        if len(temp) == 0:
            raise IndexError("There are no food supplies left!")
        return temp

    @property
    def water(self):
        temp = [s for s in self.supplies if s.__class__.__name__ == 'WaterSupply']
        if len(temp) == 0:
            raise ValueError("There are no water supplies left!")
        return temp

    @property
    def painkillers(self):
        temp = [s for s in self.medicine if s.__class__.__name__ == 'Painkiller']
        if len(temp) == 0:
            raise IndexError("There are no painkillers left!")
        return temp

    @property
    def salves(self):
        temp = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if len(temp) == 0:
            raise IndexError("There are no salves left!")
        return temp

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                pill = self.painkillers[-1]
            else:
                pill = self.salves[-1]
            survivor.health += pill.health_increase
            del self.medicine[-1]
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                soup = self.food[-1]
            else:
                soup = self.water[-1]
            survivor.needs += soup.needs_increase
            del self.supplies[-1]
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2

        for s in self.survivors:
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')

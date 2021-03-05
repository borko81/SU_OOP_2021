class Zoo:

    __slots__ = 'name, __budget, __animal_capacity, __workers_capacity, animals, workers'.split(', ')

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'

        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        temp_worker = [worker for worker in self.workers if worker.name == worker_name]
        try:
            self.workers.remove(temp_worker[0])
            return f"{worker_name} fired successfully"
        except IndexError:
            return "There is no %s in the zoo" % worker_name

    def pay_workers(self):
        temp_worker_salary = sum([worker.salary for worker in self.workers])
        if self.__budget < temp_worker_salary:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= temp_worker_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        amount_to_pay = sum((animal.get_needs() for animal in self.animals))
        if self.__budget < amount_to_pay:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= amount_to_pay
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    @staticmethod
    def __get_animal_type_list(where_to_search, animal_name):
        return [animal for animal in where_to_search if animal.__class__.__name__ == animal_name]

    def animals_status(self):
        lions = self.__get_animal_type_list(self.animals, 'Lion')
        tigers = self.__get_animal_type_list(self.animals, 'Tiger')
        cheetahs = self.__get_animal_type_list(self.animals, 'Cheetah')

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(lion.__repr__() for lion in lions)
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += '\n'.join(tiger.__repr__() for tiger in tigers)
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheeta.__repr__() for cheeta in cheetahs)
        return result

    def workers_status(self):
        keepers = self.__get_animal_type_list(self.workers, 'Keeper')
        caretaker = self.__get_animal_type_list(self.workers,'Caretaker')
        vets = self.__get_animal_type_list(self.workers,'Vet')

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(lion.__repr__() for lion in keepers)
        result += f"\n----- {len(caretaker)} Caretakers:\n"
        result += '\n'.join(tiger.__repr__() for tiger in caretaker)
        result += f"\n----- {len(vets)} Vets:\n"
        result += '\n'.join(cheeta.__repr__() for cheeta in vets)
        return result

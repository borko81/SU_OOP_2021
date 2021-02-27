from attr_and_methods.Gym.customer import Customer
from attr_and_methods.Gym.equipment import Equipment
from attr_and_methods.Gym.exercise_plan import ExercisePlan
from attr_and_methods.Gym.subscription import Subscription
from attr_and_methods.Gym.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment =[]
        self.plans = []
        self.subscriptions = []

        self._customers_by_id = {}
        self._trainers_by_id = {}
        self._equipments_by_id = {}
        self._plans_by_id = {}
        self._subscriptions_by_id = {}

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
            self._customers_by_id[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.customers.append(trainer)
            self._trainers_by_id[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.customers.append(equipment)
            self._equipments_by_id[equipment.id] = equipment

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.customers.append(plan)
            self._plans_by_id[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.customers.append(subscription)
            self._subscriptions_by_id[subscription.id] = subscription

    def subscription_info(self, subscription_id:int):
        sub = self._subscriptions_by_id[subscription_id]

        trainer = self._trainers_by_id[sub.trainer_id]
        customer = self._customers_by_id[sub.customer_id]

        plan = self._plans_by_id[sub.exercise_id]
        equipment = self._equipments_by_id[plan.equipment_id]

        return '\n'.join(map(str, [
            sub,
            customer,
            trainer,
            equipment,
            plan
        ]))


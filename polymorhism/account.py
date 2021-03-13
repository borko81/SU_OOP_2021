import unittest


class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return list(reversed(self._transactions))

    def __add__(self, other):
        user = f"{self.owner}&{other.owner}"
        acc = Account(user, amount=self.amount + other.amount)
        acc._transactions.extend(self._transactions + other._transactions)
        return acc

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ne__(self, other):
        return self.balance != other.balance


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc_one = Account('Bob', 100)
        self.acc_one.add_transaction(100)
        self.acc_two = Account('John', 150)
        self.acc_two.add_transaction(100)

    def test_set_up_correct(self):
        self.assertEqual(self.acc_one.owner, 'Bob')
        self.assertEqual(self.acc_two.owner, 'John')
        self.assertEqual(self.acc_one.amount, 100)
        self.assertEqual(self.acc_two.amount, 150)

    def test_add_one_account_to_other(self):
        acc = Account(self.acc_one.owner + '&' + self.acc_two.owner, amount=self.acc_one.amount + self.acc_two.amount)
        acc._transactions.extend(self.acc_one._transactions + self.acc_two._transactions)
        self.assertEqual(acc.amount, 250)
        self.assertEqual(acc._transactions, [100, 100])

    def test_balance(self):
        self.assertEqual(self.acc_one.balance, 200)
        self.assertEqual(self.acc_two.balance, 250)

    def test_validate_is_static_method(self):
        acquire = type(Account.validate_transaction)
        self.assertEqual(acquire.__name__, 'function')

    def test_validate_is_not_ok_shoudl_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            Account.validate_transaction(self.acc_one, -101)
        self.assertEqual(str(ex.exception), 'sorry cannot go in debt!')

    def test_validate_is_ok_inrese_amount(self):
        Account.validate_transaction(self.acc_one, 100)
        self.assertEqual(self.acc_one._transactions, [100, 100])


if __name__ == '__main__':
    acc = Account('Bob', 100)
    # print(type(Account.validate_transaction))
    unittest.main()

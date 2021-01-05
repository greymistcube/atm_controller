import random
from bank import Bank

class MockAccount:
    def __init__(self, number: str, balance: int):
        self._number = number
        self._balance = balance
        return

    def deposit(self, amount: int):
        self._balance += amount
        return

    def withdraw(self, amount: int):
        self._balance -= amount

    @property
    def number(self) -> str:
        return self._number

    @property
    def balance(self) -> int:
        return self._balance

    @classmethod
    def generate_mock_number(self) -> str:
        return f"{random.randint(0, 99999999):08d}"

    @classmethod
    def generate_mock_balance(Self) -> int:
        return random.randint(0, 1000)

class MockCard:
    def __init__(self, number: str, pin: str, accounts: list):
        self._number = number
        self._pin = pin
        self._accounts = accounts
        return

    @property
    def number(self) -> str:
        return self._number

    @property
    def pin(self) -> str:
        return self._pin

    @property
    def accounts(self) -> list:
        return self._accounts

class MockBank(Bank):
    def __init__(self):
        super().__init__()
        self._card: MockCard
        return

    def check_pin(self, card: str, pin: str) -> bool:
        check = random.randint(0, 1)
        if check:
            # dynamically generate a mock card for testing
            accounts = [
                MockAccount(
                    number=MockAccount.generate_mock_number(),
                    balance=MockAccount.generate_mock_balance(),
                ) for _ in range(random.randint(1, 4))
            ]
            self._card = MockCard(card, pin, accounts)
            return True
        else:
            return False

    def get_accounts(self, card: str) -> list:
        return [account.number for account in self._card.accounts]

    def get_balance(self, card: str, account: str) -> int:
        pass

    def make_deposit(self, card: str, account: str, amount: int) -> bool:
        pass

    def make_withdrawal(self, card: str, account: str, amount: str) -> bool:
        pass

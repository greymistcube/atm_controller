import random
from bank import Bank

class MockAccount:
    def __init__(self, account_number: str, balance: int):
        self._number = account_number
        self._balance = balance
        return

    @property
    def number(self) -> str:
        return self._number

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, other) -> None:
        self._balance = other
        return

    @classmethod
    def generate_mock_number(self) -> str:
        return f"{random.randint(0, 99999999):08d}"

    @classmethod
    def generate_mock_balance(cls) -> int:
        return random.randint(0, 1000)

class MockCard:
    def __init__(self, card_number: str, pin_number: str, accounts: dict):
        self._number = card_number
        self._pin = pin_number
        self._accounts = accounts
        return

    def get_account(self, account_number: str) -> MockAccount:
        return self._accounts[account_number]

    @property
    def number(self) -> str:
        return self._number

    @property
    def pin(self) -> str:
        return self._pin

    @property
    def accounts(self) -> dict:
        return self._accounts

    @classmethod
    def generate_mock_accounts(cls) -> dict:
        accounts = {}
        for _ in range(random.randint(1, 4)):
            mock_number = MockAccount.generate_mock_number()
            mock_balance = MockAccount.generate_mock_balance()
            accounts[mock_number] = MockAccount(
                account_number=mock_number,
                balance=mock_balance,
            )
        return accounts

class MockBank(Bank):
    def __init__(self):
        super().__init__()
        self._cards = {}
        return

    def check_pin(self, card_number: str, pin_number: str) -> bool:
        check = random.randint(0, 1)
        if check:
            # dynamically generate a mock card for testing
            if card_number not in self._cards:
                self._cards[card_number] = MockCard(
                    card_number=card_number,
                    pin_number=pin_number,
                    accounts=MockCard.generate_mock_accounts(),
                )
            return True
        else:
            return False

    def get_accounts(self, card_number: str) -> list:
        card = self._cards[card_number]
        return [account.number for account in card.accounts.values()]

    def get_balance(
        self,
        card_number: str,
        account_number: str,
    ) -> int:
        card = self._cards[card_number]
        account = card.accounts[account_number]
        balance = account.balance
        return balance

    def make_deposit(
        self,
        card_number: str,
        account_number: str,
        amount: int,
    ) -> bool:
        card = self._cards[card_number]
        account = card.accounts[account_number]
        account.balance = account.balance + amount
        return True

    def make_withdrawal(
        self,
        card_number: str,
        account_number: str,
        amount: str,
    ) -> bool:
        card = self._cards[card_number]
        account = card.accounts[account_number]
        if account.balance > amount:
            account.balance = account.balance - amount
            return True
        else:
            return False

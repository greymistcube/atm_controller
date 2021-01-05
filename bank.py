import abc

class Bank(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def check_pin(self, card: str, pin: str) -> bool:
        pass

    @abc.abstractmethod
    def get_accounts(self, card: str) -> list:
        pass

    @abc.abstractmethod
    def get_balance(self, card: str, account: str) -> int:
        pass

    @abc.abstractmethod
    def make_deposit(self, card: str, account: str, amount: int) -> bool:
        pass

    @abc.abstractmethod
    def make_withdrawal(self, card: str, account: str, amount: str) -> bool:
        pass

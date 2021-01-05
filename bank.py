import abc

class Bank(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def check_pin(self, card_number: str, pin_number: str) -> bool:
        pass

    @abc.abstractmethod
    def get_accounts(self, card_number: str) -> list:
        pass

    @abc.abstractmethod
    def get_balance(
        self,
        card_number: str,
        account_number: str,
    ) -> int:
        pass

    @abc.abstractmethod
    def make_deposit(
        self,
        card_number: str,
        account_number: str,
        amount: int,
    ) -> bool:
        pass

    @abc.abstractmethod
    def make_withdrawal(
        self,
        card_number: str,
        account_number: str,
        amount: str,
    ) -> bool:
        pass

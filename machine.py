import abc

class Machine(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def insert_card(self) -> str:
        pass

    @abc.abstractmethod
    def enter_pin(self) -> str:
        pass

    @abc.abstractmethod
    def select_account(self, accounts: list) -> int:
        pass

    @abc.abstractmethod
    def select_action(self) -> int:
        pass

    @abc.abstractmethod
    def balance(self, balance: int) -> None:
        pass

    @abc.abstractmethod
    def deposit(self) -> int:
        pass

    @abc.abstractmethod
    def withdraw(self) -> int:
        pass

    @abc.abstractmethod
    def eject_card(self) -> None:
        pass

    @abc.abstractmethod
    def error(self) -> None:
        pass

    @abc.abstractmethod
    def print_message(self, message: str) -> None:
        pass

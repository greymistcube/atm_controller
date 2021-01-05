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
    def select_account(self, accounts) -> str:
        pass

    @abc.abstractmethod
    def select_action(self) -> str:
        pass

    @abc.abstractmethod
    def eject_card(self) -> None:
        pass

    @abc.abstractmethod
    def print_message(self, message: str) -> None:
        pass

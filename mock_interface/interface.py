import abc

class ATMInterface(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def insert_card(self) -> str:
        pass

    @abc.abstractmethod
    def get_pin(self) -> str:
        pass

    @abc.abstractmethod
    def get_account(self) -> str:
        pass

    @abc.abstractmethod
    def get_action(self) -> str:
        pass

    @abc.abstractmethod
    def eject_card(self) -> None:
        pass

class MockATMInterface(ATMInterface):
    def __init__(self):
        super().__init__()
        return

    def insert_card(self) -> str:
        while True:
            card = input("insert card (12 digits): ")
            if card.isnumeric() and len(card) == 12:
                break
            else:
                print("invalid format; please try again")
                continue
        return card

    def get_pin(self) -> str:
        while True:
            pin = input("enter pin (4 digits): ")
            if pin.isnumeric and len(pin) == 4:
                break
            else:
                print("invalid format; please try again")
                continue
        return pin

    def get_account(self, accounts) -> str:
        for i, account in enumerate(accounts):
            print(f"{i}. {account}")
        print(f"{len(accounts)}. Cancel")
        while True:
            option = input(f"select account (0 ~ {len(accounts) - 1})")
            if option.isnumeric and int(option) <= len(accounts):
                break
            else:
                print("invalid option; please try again")
                continue
        return option

    def get_action(self) -> str:
        print("0. Check Balance")
        print("1. Deposit Cash")
        print("2. Withdraw Cash")
        print("3. Cancel")
        while True:
            option = input("select action (0 ~ 3): ")
            if option.isnumeric and int(option) <= 3:
                break
            else:
                print("invalid option; please try again")
                continue
        return option

    def eject_card(self) -> None:
        pass

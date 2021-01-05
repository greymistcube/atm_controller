from machine import Machine

class MockMachine(Machine):
    def __init__(self):
        super().__init__()
        return

    def insert_card(self) -> str:
        print("")
        print("==================")
        print("INSERT CARD SCREEN")
        print("==================")
        while True:
            card = input("insert card (12 digits): ")
            if card.isnumeric() and len(card) == 12:
                break
            else:
                print("invalid format; please try again")
                continue
        return card

    def enter_pin(self) -> str:
        print("")
        print("================")
        print("PIN ENTER SCREEN")
        print("================")
        while True:
            pin = input("enter pin (4 digits): ")
            if pin.isnumeric and len(pin) == 4:
                break
            else:
                print("invalid format; please try again")
                continue
        return pin

    def select_account(self, accounts) -> str:
        print("")
        print("=====================")
        print("SELECT ACCOUNT SCREEN")
        print("=====================")
        for i, account in enumerate(accounts):
            print(f"{i}. {account}")
        print(f"{len(accounts)}. Cancel")
        while True:
            option = input(f"select account (0 ~ {len(accounts)}): ")
            if option.isnumeric and int(option) <= len(accounts):
                break
            else:
                print("invalid option; please try again")
                continue
        return option

    def select_action(self) -> str:
        print("")
        print("====================")
        print("SELECT ACTION SCREEN")
        print("====================")
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
        print("")
        print("=================")
        print("EJECT CARD SCREEN")
        print("=================")
        input("please retrieve your card (press enter)")
        print("bye")
        return

    def print_message(self, message: str) -> None:
        print(message)
        return

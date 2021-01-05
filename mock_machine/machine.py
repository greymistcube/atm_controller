import time
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
            if pin.isnumeric() and len(pin) == 4:
                break
            else:
                print("invalid format; please try again")
                continue
        return pin

    def select_account(self, accounts: list) -> int:
        print("")
        print("=====================")
        print("SELECT ACCOUNT SCREEN")
        print("=====================")
        for i, account in enumerate(accounts):
            print(f"{i}. {account}")
        print(f"{len(accounts)}. Cancel")
        while True:
            option = input(f"select account (0 ~ {len(accounts)}): ")
            if option.isnumeric() and int(option) <= len(accounts):
                break
            else:
                print("invalid option; please try again")
                continue
        return int(option)

    def select_action(self) -> int:
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
            if option.isnumeric() and int(option) <= 3:
                break
            else:
                print("invalid option; please try again")
                continue
        return int(option)

    def balance(self, balance: int) -> int:
        print("")
        print("==============")
        print("BALANCE SCREEN")
        print("==============")
        print(f"balance: {balance}")
        return

    def deposit(self) -> int:
        print("")
        print("==============")
        print("DEPOSIT SCREEN")
        print("==============")
        while True:
            amount = input("enter deposit amount: ")
            if amount.isnumeric():
                break
            else:
                print("invalid amount; please try again")
                continue
        return int(amount)

    def withdraw(self) -> int:
        print("")
        print("===============")
        print("WITHDRAW SCREEN")
        print("===============")
        while True:
            amount = input("enter withdraw amount: ")
            if amount.isnumeric():
                break
            else:
                print("invalid amount; please try again")
                continue
        return int(amount)

    def eject_card(self) -> None:
        print("")
        print("=================")
        print("EJECT CARD SCREEN")
        print("=================")
        input("please retrieve your card (press enter)")
        print("bye")
        return

    def error(self) -> None:
        print("")
        print("============")
        print("ERROR SCREEN")
        print("============")
        print("something went terribly wrong")
        print("please contant an admin")
        while True:
            time.sleep(60)
        return

    def print_message(self, message: str) -> None:
        print(message)
        return

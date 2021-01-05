from bank import Bank
from machine import Machine

class Session:
    def __init__(self, bank: Bank, machine: Machine):
        self._bank = bank
        self._machine = machine
        return

    def run(self):
        card = self._machine.insert_card()

        for _ in range(3):
            pin = self._machine.enter_pin()
            check = self._bank.check_pin(card, pin)
            if check:
                self._machine.print_message("pin valid")
                break
            else:
                self._machine.print_message("pin invalid")
                continue

        if check:
            account = self._select_account(card)
            action = self._select_action()
        else:
            self._machine.print_message("too many invalid pin attempts")
            self._machine.eject_card()
        return

    def _select_account(self, card: str) -> str:
        accounts = self._bank.get_accounts(card)
        account = self._machine.select_account(accounts)
        return account

    def _select_action(self) -> str:
        return self._machine.select_action()

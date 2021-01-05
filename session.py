from bank import Bank
from machine import Machine

MAX_PIN_ATTEMPTS = 3

class TooManyPinAttemptsError(Exception):
    pass

class Session:
    def __init__(self, bank: Bank, machine: Machine):
        self._bank = bank
        self._machine = machine
        return

    def run_session(self):
        try:
            card = self._machine.insert_card()
            try:
                self._check_pin(card)
            except TooManyPinAttemptsError:
                self._machine.print_message("too many invalid pin attempts")
                self._machine.eject_card()
                return

            self._run_card(card)
        except:
            self._error()
        return

    def _check_pin(self, card: str) -> None:
        for _ in range(MAX_PIN_ATTEMPTS):
            pin = self._machine.enter_pin()
            check = self._bank.check_pin(card, pin)
            if check:
                return
            else:
                self._machine.print_message("pin invalid")
                continue
        raise TooManyPinAttemptsError("too many invalid pin attempts")

    def _run_card(self, card: str):
        while True:
            account = self._select_account(card)
            if account:
                self._run_account(card, account)
            else:
                break
        return

    def _run_account(self, card: str, account: str):
        action = self._select_action()
        if action:
            action(card, account)
        return

    def _select_account(self, card: str) -> str:
        accounts = self._bank.get_accounts(card)
        account_index = self._machine.select_account(accounts)
        try:
            return accounts[account_index]
        except:
            return ""

    def _select_action(self) -> callable:
        actions = {
            0: self._check_balance,
            1: self._make_deposit,
            2: self._make_withdrawal,
            3: None,
        }
        action_index = self._machine.select_action()
        action = actions[action_index]
        return action

    def _check_balance(self, card: str, account: str) -> str:
        balance = self._bank.get_balance(card, account)
        self._machine.balance(balance)
        return

    def _make_deposit(self, card: str, account: str) -> str:
        amount = self._machine.deposit()
        result = self._bank.make_deposit(card, account, amount)
        if result:
            self._machine.print_message("deposit successful")
        else:
            self._machine.print_message("deposit failed")
        return

    def _make_withdrawal(self, card: str, account: str) -> str:
        amount = self._machine.withdraw()
        result = self._bank.make_withdrawal(card, account, amount)
        if result:
            self._machine.print_message("withdraw successful")
        else:
            self._machine.print_message("withdraw failed")
        return

    def _error(self) -> None:
        self._machine.error()
        return

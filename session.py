class Session:
    def __init__(self, bank, machine):
        self._bank = bank
        self._machine = machine
        return

    def run(self):
        card = self._machine.insert_card()
        pin = self._machine.enter_pin()
        return

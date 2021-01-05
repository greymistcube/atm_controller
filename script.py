from mock_bank.bank import MockBank
from mock_machine.machine import MockMachine
from session import Session

if __name__ == "__main__":
    bank = MockBank()
    machine = MockMachine()

    while True:
        session = Session(bank, machine)
        session.run_session()
    exit()

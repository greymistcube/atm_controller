import abc

class Bank(abc.ABC):
    pass

class MockBank(Bank):
    def __init__(self):
        super().__init__()
        return


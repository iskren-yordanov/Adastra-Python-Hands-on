class MyError(Exception):
    pass


class BankAccount():

    def __init__(self, account_number, date_open, interest_rate, opening_balance):
        self._account_number = account_number
        self._date_open = date_open
        self._interest_rate = interest_rate
        self._balance = opening_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> None:
        pass

    def withraw(self, amount: float) -> None:
        pass

    def transfer(self, second_account: object) -> None:
        pass

# test are located in folder tests/tests_bank_account.py file
    
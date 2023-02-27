from Esquemas.Account import account
from Esquemas.Users import User
from datetime import datetime


class AccountController:
    @staticmethod
    def create_account(user:str,card:str,limit_date:datetime,balance:float,credit_limit:float,remaining_credit:float,minimum:float,minimum_interest:float,Status_BC:bool,usage:float) -> account:
        new_account = account(user = user,
                              card=card,
                              Balance = balance,
                              limit_date=limit_date,
                              credit_limit = credit_limit,
                              remaining_credit=remaining_credit,
                              minimum=minimum,
                              minimum_interest=minimum_interest,
                              Status_BC = Status_BC,
                              usage=usage)
        new_account.save()
        return new_account


class CreditCard:
    def __init__(self, user: str, credit_limit: float, usage: float):
        self.user = user
        self.credit_limit = credit_limit
        self.usage = usage

    def get_available_credit(self):
        return self.credit_limit - self.usage

    def spend(self, amount: float):
        if amount < self.credit_limit:
            self.usage = self.usage + amount

        else:
            raise ValueError("Insufficient funds")

    def pay(self, amount: float):
        self.usage = self.usage - amount

pass
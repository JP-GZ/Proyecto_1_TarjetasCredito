from Esquemas.Account import Account
from Esquemas.Card_info import Card
from Esquemas.Users import User
from datetime import datetime


class AccountController:
    @staticmethod
    def create_account(user_id: User, limit_date: datetime,
                       minimum: float, minimum_interest: float, Status_BC: bool, usage: float) -> Account:
        new_account = Account(user_id=user_id,
                              balance=.08 * user_id.estimated_income,
                              limit_date=limit_date,
                              credit_limit=.8 * user_id.estimated_income, # No se usa
                              remaining_credit=0,# No se usa
                              minimum=minimum,
                              minimum_interest=minimum_interest,
                              status_BC=Status_BC,
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

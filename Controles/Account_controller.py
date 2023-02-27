from Esquemas.Account import account
from Esquemas.Users import User
from datetime import datetime


class AccountController:
    @staticmethod
    def create_account(balance:float,credit_limit:float,cutoff_date:datetime,estimated_income:float,Status_BC=bool) -> account:
        new_account = account(Balance = balance,
                       Credit_limit = credit_limit,
                       Cutoff_date = cutoff_date,
                       Estimated_income = estimated_income,
                       Status_BC = Status_BC)
        new_account.save()
        return new_account
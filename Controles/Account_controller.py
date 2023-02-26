from datetime import  datetime
from Esquemas.Account import account as ac


class account_controll:

    def add_account(balance:int,cred_lim:int,date:datetime,income:int,BC:bool):
        account = ac(
        balance=balance,
        credit_limit = cred_lim,
        cutoff_date = date,
        estimated_income = income,
        Status_BC = BC,
        )
        account.save()
        return account
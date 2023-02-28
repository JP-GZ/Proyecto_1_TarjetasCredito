from datetime import datetime

from Esquemas.Account import Account
from Esquemas.Payments import Payment
from Esquemas.Users import User
from Esquemas.Transactions import Transaction


class TransactionController:
    @staticmethod
    def add_transaction(account_id: str, date_time: str, amount: float):
        transaction = Transaction(
            account_id=account_id,
            date_time=date_time,
            amount=amount
        )
        transaction.save()

        acc = Account.select().where(Account.id == account_id.id).get()
        if amount < acc.balance:
            acc.balance -= amount
            acc.save()
        else:
            print("No mames de donde")

        return transaction

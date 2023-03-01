from datetime import datetime

from Esquemas.Account import Account
from Esquemas.Payments import Payment
from Esquemas.Users import User
from Esquemas.Transactions import Transaction


class TransactionController:
    @staticmethod
    def add_transaction(account_id: str, date_time: str, amount: float):
        # Get the account
        acc = Account.select().where(Account.id == account_id.id).get()
        # Check the balance, if the amount is bigger than the balance
        # we will not create the transaction and throw an error
        if amount > acc.balance:
            raise ValueError("No mames de donde")

        acc.balance -= amount
        acc.save()

        transaction = Transaction(
            account_id=account_id,
            date_time=date_time,
            amount=amount
        )
        transaction.save()
        return transaction

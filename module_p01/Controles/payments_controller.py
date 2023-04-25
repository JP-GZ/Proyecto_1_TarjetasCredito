from datetime import datetime

from Esquemas.Account import Account
from Esquemas.Payments import Payment
from Esquemas.Users import User


class PaymentController:
    @staticmethod
    def add_payment(account_id: str, date_time: datetime, amount: float):
        payment = Payment(
            account_id=account_id,
            date_time=date_time,
            amount=amount
        )
        payment.save()


        acc = Account.select().where(Account.id == account_id.id).get()
        acc.balance += amount
        acc.save()
        return payment

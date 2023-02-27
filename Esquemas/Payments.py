from peewee import *
from Esquemas.Account import account

db = SqliteDatabase("./db/Credit_cards.db")


class Payment(Model):
    account_id = ForeignKeyField(account, backref="payments")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db



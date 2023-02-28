from peewee import *
from Esquemas.Account import Account

db = SqliteDatabase("./db/Credit_cards.db")


class Payment(Model):
    account_id = ForeignKeyField(Account, backref="payments")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db



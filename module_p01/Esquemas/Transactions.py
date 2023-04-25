from peewee import *

from Esquemas.Account import Account
from Esquemas.Card_info import Card

db = SqliteDatabase("./db/Credit_cards.db")


class Transaction(Model):
    account_id = ForeignKeyField(Account, backref="transactions")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db
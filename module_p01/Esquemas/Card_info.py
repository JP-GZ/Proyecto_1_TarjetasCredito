import random
from peewee import *

from Esquemas.Account import Account
from Esquemas.Users import User

db = SqliteDatabase("./db/Credit_cards.db")


class Card(Model):
    name_id = ForeignKeyField(Account, backref='cards')
    plastic = CharField()  # Unique
    cvv = CharField()
    date_expired = DateTimeField()
    NIP = CharField()

    class Meta:
        database = db

from peewee import *
from Esquemas.Card_info import card

db = SqliteDatabase("./db/Credit_cards.db")


class transaction(Model):
    card_id = ForeignKeyField(card, backref="charges")
    date_time = DateTimeField()
    amount = FloatField()

    class Meta:
        database = db
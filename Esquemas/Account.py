from peewee import *
from Esquemas.Users import User
from Esquemas.Card_info import card
db = SqliteDatabase("./db/Credit_cards.db")

class account(Model):
    user = ForeignKeyField(User,backref='User')
    card = ForeignKeyField(card,backref="User")
    balance = CharField()
    limit_date=DateTimeField()
    credit_limit = CharField()
    remaining_credit = FloatField()
    minimum = FloatField()
    minimum_interest = FloatField()
    status_BC = BooleanField()
    usage = FloatField()

    class Meta:
        database = db















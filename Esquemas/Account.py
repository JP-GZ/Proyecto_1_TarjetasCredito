from peewee import *
from Esquemas.Users import User
from Esquemas.Card_info import card_info
db = SqliteDatabase('Credict_cards.db')

class account(Model):
    balance = CharField()
    credit_limit = CharField()
    cutoff_date = DateTimeField()
    estimated_income = DateTimeField()
    Status_BC = BooleanField()

    class Meta:
        database = db















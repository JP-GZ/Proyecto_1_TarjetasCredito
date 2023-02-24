import random
from peewee import *
from Esquemas.Users import User
db = SqliteDatabase('Credict_cards.db')


class card_info(Model):
    User_name = CharField(User)
    User_name = CharField(User)
    Num_plastic = CharField(unique=True)
    cvv = CharField()
    date_expired = CharField()
    NIP = CharField()

    class Meta:
        database = db

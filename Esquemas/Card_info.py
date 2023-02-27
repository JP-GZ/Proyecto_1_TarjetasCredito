import random
from peewee import *
from Esquemas.Users import User

db = SqliteDatabase("./db/Credit_cards.db")


class card(Model):
    User_name = ForeignKeyField(User,backref='User')
    Num_plastic = CharField() #Unique
    cvv = CharField()
    date_expired = DateTimeField()
    NIP = CharField()

    class Meta:
        database = db


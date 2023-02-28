from peewee import *
from Esquemas.Users import User

db = SqliteDatabase("./db/Credit_cards.db")


class Account(Model):
    user_id = ForeignKeyField(User, backref='accounts')
    balance = FloatField()
    limit_date = DateTimeField()
    credit_limit = CharField()
    remaining_credit = FloatField()
    minimum = FloatField()
    minimum_interest = FloatField()
    status_BC = BooleanField()
    usage = FloatField()

    class Meta:
        database = db

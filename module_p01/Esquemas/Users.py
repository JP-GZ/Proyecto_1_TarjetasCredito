from peewee import *

db = SqliteDatabase("./db/Credit_cards.db")

class User(Model):
    Name = CharField()
    Birthdate = DateTimeField() # Cambiar a tipo datetime
    RFC = CharField()
    Address = CharField()
    Curp = CharField()
    Phone = CharField()
    Email = CharField()
    account = CharField()
    password = CharField()
    estimated_income = FloatField()

    class Meta:
        database = db
from peewee import *

db = SqliteDatabase('Credict_cards.db')

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

    class Meta:
        database = db
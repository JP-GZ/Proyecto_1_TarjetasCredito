from peewee import *

db = SqliteDatabase('Credict_cards.db')

class User(Model):
    First_name = CharField()
    Second_name = CharField()
    Last_name = CharField()
    Birthdate = CharField() # Cambiar a tipo datetime
    User_RFC = CharField()
    User_Curp = CharField()
    User_Phone = CharField()
    Email = CharField()
    account = CharField()
    password = CharField()

    class Meta:
        database = db
from peewee import *

db = SqliteDatabase('Credict_cards.db')

class User(Model):
    User_ID = AutoField()
    First_name = CharField()
    Second_name = CharField()
    Last_name = CharField()
    Birthdate = DateField(formats = '%Y-%m-%d')
    User_RFC = CharField(unique=True)
    User_Curp = CharField(unique=True)
    User_Phone = CharField(unique=True)
    Email = CharField(unique=True)
    User_account = CharField()
    User_password =  CharField()
    class Meta:
        database = db
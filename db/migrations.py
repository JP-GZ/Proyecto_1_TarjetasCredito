from peewee import SqliteDatabase

from Esquemas.Users import User
from Esquemas.Card_info import card
from Esquemas.Account import account

db = SqliteDatabase('Credit_cards.db')
db.create_tables([User,card,account])

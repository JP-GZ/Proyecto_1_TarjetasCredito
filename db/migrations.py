from peewee import SqliteDatabase

from Esquemas.Users import User
from Esquemas.Card_info import card_info
from Esquemas.Account import account

db = SqliteDatabase('Credict_cards.db')
db.create_tables([User, card_info, account])
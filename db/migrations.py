from peewee import SqliteDatabase

from Esquemas.Users import User
from Esquemas.Card_info import Card
from Esquemas.Account import Account
from Esquemas.Payments import Payment
from Esquemas.Transactions import Transaction
import os

print("Connecting DB...")
print(os.path.abspath("."))
db = SqliteDatabase('Credit_cards.db')
db.create_tables([User, Card, Account, Payment, Transaction])

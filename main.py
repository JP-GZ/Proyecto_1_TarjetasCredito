from datetime import datetime, timedelta
import faker

from Controles.Card_info_controller import Cardinfo_controller as CC
from Controles.Account_controller import AccountController as AC
from Controles.user_controller import UserController as UC
from Controles.payments_controller import PaymentController as PC
from Controles.transactions_controller import TransactionController as TC

from db import migrations

from Esquemas.Users import User
from Esquemas.Card_info import Card as CI
from Esquemas.Account import Account as AT
from Esquemas.Payments import Payment
from Esquemas.Transactions import Transaction

# TODO: Ya aqui va todo lo solicitado
# Se supone que con solo ingresar el usuario y el ingreso estimado la tarjetas se
# deberan generar de manera automatica junto a su balance

name = 'Juan Pablo Garcia Zaragoza'
Birthdate = '1998-06-30'
RFC = 'GALJ980630'
Curp = 'GALJ980630'
phone = '3314564674'
email = 'if722489@iteso'
account = 'JPGZ'
password = '123456'
estimated_income = 150000.00
now = datetime.now()

user = UC.create_user(name=name,
                      Birthdate=Birthdate,
                      RFC=RFC,
                      Curp=Curp,
                      phone=phone,
                      email=email,
                      account=account,
                      password=password,
                      estimated_income=estimated_income,
                      Address="Av 1234"
                      )
cuenta = AC.create_account(
    user_id=user,
    limit_date=datetime(now.year, now.month, now.day) + timedelta(days=20),
    minimum=0,
    minimum_interest=0,
    Status_BC=True,
    usage=0
)

card = CC.add_cardinfo(name_id=cuenta,
                       plastic=CC.generador_plastico(),
                       cvv=CC.cvv(),
                       date=datetime(now.year + 5, now.month, 1),
                       NIP=CC.NIP()
                       )








print("Nombre y RFC usuario:")
for u in User.select():
    print(u.id,u.Name, u.RFC)
print("Tarjeta Asociada:")
for c in CI.select():
    print(c.id, c.name_id, c.plastic)
transaccion = TC.add_transaction(
    account_id=cuenta,
    date_time=cuenta.limit_date,
    amount=130
)
print(f'Compra por:',transaccion.amount)

print("Balance Usuario:")
for a in AT.select():
    print(a.id,a.balance)

payment = PC.add_payment(
    account_id=cuenta,
    date_time=cuenta.limit_date,
    amount=130
)
print(f'Abono por:',payment.amount)
print("Balance Usuario:")
for a in AT.select():
    print(a.id,a.balance)

User.delete().execute()
CI.delete().execute()
AT.delete().execute()
Payment.delete().execute()
Transaction.delete().execute()
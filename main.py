from datetime import datetime

from Simulador.Simulador import simulador
from Controles.Card_info_controller import Cardinfo_controller as CC
from Controles.Account_controller import AccountController as AC
from Controles.user_controller import UserController as UC

from db import migrations

from Esquemas.Users import User
from Esquemas.Card_info import card as CI
from Esquemas.Account import account as AT

# TODO: Ya aqui va todo lo solicitado
# Se supone que con solo ingresar el usuario y el ingreso estimado la tarjetas se
# deberan generar de manera automatica junto a su balance

migrations

# user2 = UC.create_user(name='Juan Pablo Garcia Zaragoza',
#                        Birthdate='1998-06-30',
#                        RFC='GALJ980630',
#                        Curp='GALJ980630',
#                        phone='3314564674',
#                        email='if722489@iteso',
#                        account='JPGZ',
#                        password='123456')


#for u in User.select():
#    print(u.First_name,u.User_RFC)



# En teoria debido a que los datos contienen datos unicos
# la base no se debe de agregar 2 veces el mismo nombre
# con los mismos datos

print(simulador.generador_plastico(1))

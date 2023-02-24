import random
from peewee import *
from Esquemas.Users import User
db = SqliteDatabase('Credict_cards.db')


class card_info(Model):
    User_name = CharField(User)
    User_name = CharField(User)
    Num_plastic = CharField(unique=True)
    cvv = CharField()
    date_expired = CharField()
    NIP = CharField()

    class Meta:
        database = db
def generador_plastico():
    # Generar el primer dígito aleatorio entre 3 y 6 (para tarjetas de crédito)
    primer_digito = '4' + str(random.randint(3, 6))
    siguientes_digitos = "".join([str(random.randint(0, 9)) for i in range(13)])
    numero_tarjeta = primer_digito + siguientes_digitos
    # Agregar un dígito de verificación (checksum) al final del número de tarjeta
    suma_digitos = 0
    for i in range(len(numero_tarjeta)):
        digito = int(numero_tarjeta[i])
        if i % 2 == 0:
            digito *= 2
            if digito > 9:
                digito -= 9
        suma_digitos += digito
    digito_verificacion = (10 - (suma_digitos % 10)) % 10
    numero_tarjeta += str(digito_verificacion)
    return (numero_tarjeta)

def cvv():
    return ("".join([str(random.randint(0, 9)) for i in range(3)]))
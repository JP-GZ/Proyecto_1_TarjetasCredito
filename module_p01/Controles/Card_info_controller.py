from Esquemas.Card_info import Card as cd
from Esquemas.Users import User
import random
from datetime import datetime


class Cardinfo_controller:
    @staticmethod
    def add_cardinfo(name_id: str, plastic: str, cvv: str, date: datetime, NIP: str):
        Card_info = cd(name_id=name_id,
                       plastic=plastic,
                       cvv=cvv,
                       date_expired=date,
                       NIP=NIP)
        Card_info.save()

        return Card_info

    @staticmethod
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

    @staticmethod
    def cvv():
        return ("".join([str(random.randint(0, 9)) for i in range(3)]))

    @staticmethod
    def NIP():
        return '1234'  # ("".join([str(random.randint(0, 9)) for i in range(4)]))

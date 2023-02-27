
from Esquemas.Card_info import card as cd
from Esquemas.Users import User
import random
from datetime import datetime


class Cardinfo_controller:
    @staticmethod
    def add_cardinfo(Name:str,plastic:str,cvv:str,date:datetime,NIP:str):
        Card_info = cd(User_name = Name,
                       Num_plastic = plastic,
                       cvv = cvv,
                       date_expired = date,
                       NIP = NIP)
        Card_info.save()
        return Card_info


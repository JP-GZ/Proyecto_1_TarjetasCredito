from Esquemas.Users import User
from datetime import datetime


class UserController:

    @staticmethod
    def create_user(name: str, Birthdate: str, RFC: str, Curp: str, phone: str, email: str, account: str,
                    password: str):
        new_user = User(First_name=name.split()[0],
                        Second_name=name.split()[1],
                        Last_name=" ".join(name.split()[-2:]),
                        Birthdate=Birthdate,
                        User_RFC=RFC,
                        User_Curp=Curp,
                        User_Phone=phone,
                        Email=email,
                        account=account,
                        password=password)
        new_user.save()
        return new_user

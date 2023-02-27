from Esquemas.Users import User
from datetime import datetime


class UserController:

    @staticmethod
    def create_user(name: str, RFC: str,Birthdate: datetime,Address:str,Curp: str, phone: str, email: str, account: str,
                    password: str):
        new_user = User(Name=name,
                        RFC=RFC,
                        Birthdate=Birthdate,
                        Address=Address,
                        Curp=Curp,
                        Phone=phone,
                        Email=email,
                        account=account,
                        password=password)
        new_user.save()
        return new_user

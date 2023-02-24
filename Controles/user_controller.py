from Esquemas.Users import User


class UserController:

    @staticmethod
    def create_user(name: str, Birthdate: str, RFC: str,Curp:str,phone:str,email:str,account:str,password:str) -> User:
        new_user =User(
        First_name= name.split()[0],
        Second_name = name.split()[1],
            #TODO: Si el nimbre no tiene segundo nombre agregar una condicional
        Last_name =" ".join(name.split()[-2:]),
        Birthdate = Birthdate,
        User_RFC =RFC,
        User_Curp =Curp,
        User_Phone =phone,
        Email =email,
        account =account,
        password =password
     )
        new_user.save()
        return new_user

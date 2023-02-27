from datetime import datetime
from Controles.user_controller import UserController
from Esquemas.Users import User
from db import migrations

def test_create_user():
    # Arrange
    migrations
    user = UserController.create_user(name= "Luisito",Birthdate="03-07-2000",RFC="XAXX010101000",Address='por ahi',Curp="XXXX000703XXXXXX",
                                      phone="3314778442",email="luis@hotmail.com",account="XXXXXXX",password="luis123")

    # Act
    created_user = User.select().where(User.id == user.id).get()
    # Assert
    assert user.id == created_user.id
    assert user.Name == created_user.Name
    assert user.Birthdate == created_user.Birthdate
    assert user.Address == created_user.Address
    assert user.RFC == created_user.RFC
    assert user.Curp == created_user.Curp
    assert user.Phone == created_user.Phone
    assert user.Email == created_user.Email
    assert user.account == created_user.account
    assert user.password == created_user.password

    # Delete test instances




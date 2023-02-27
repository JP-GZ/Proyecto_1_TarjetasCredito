from datetime import datetime
from Controles.user_controller import UserController
from Esquemas.Users import User

def test_create_user():
    # Arrange
    user = UserController.create_user(name= "Luisito",Birthdate="03-07-2000",RFC="XAXX010101000",Curp="XXXX000703XXXXXX",
                                      phone="3314778442",email="luis@hotmail.com",account="XXXXXXX",password="luis123")

    # Act
    created_user = User.select().where(User.id == user.id).get()

    # Assert
    assert user.id == created_user.id
    assert user.name == created_user.name
    assert user.Birthdate == created_user.Birthdate
    assert user.RFC == created_user.RFC
    assert user.Curp == created_user.Curp
    assert user.phone == created_user.phone
    assert user.email == created_user.email
    assert user.account == created_user.account
    assert user.password == created_user.password

    # Delete test instances
    created_user.delete_instance()



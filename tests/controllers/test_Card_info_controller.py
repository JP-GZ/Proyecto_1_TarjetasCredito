from datetime import datetime
from Controles.Card_info_controller import Cardinfo_controller
from Esquemas.Card_info import card
from db import migrations

def test_create_card():
    # Arrange
    migrations
    cardinfo = Cardinfo_controller.add_cardinfo(name="Luisillo",plastic=card.generador_plastico(),cvv=card.cvv(),date="02/23",NIP=card.NIP())

    # Act
    add_cardinfo = card.select().where(card.id == cardinfo.id).get()
    # Assert
    assert cardinfo.id == add_cardinfo.id
    assert cardinfo.User_name == add_cardinfo.User_name
    assert cardinfo.Num_plastic == add_cardinfo.Num_plastic
    assert cardinfo.cvv == add_cardinfo.cvv
    assert cardinfo.date_expired == add_cardinfo.date_expired
    assert cardinfo.NIP == add_cardinfo.NIP

from datetime import datetime
from Controles.Account_controller import AccountController
from Controles.Account_controller import CreditCard
from Esquemas.Account import account
from Esquemas.Users import User
from Esquemas.Card_info import card
from db import migrations

def test_create_account():
    # Arrange
    migrations
    account = AccountController.create_account(user=User,card=card.generador_plastico(),cvv=card.cvv(),limit_date=datetime(2023, 2, 1, 10, 10, 0),
                                               balance=CreditCard.get_available_credit(),credit_limit=CreditCard.credit_limit,
                                               remaining_credit=CreditCard.spend(),minimum=CreditCard.pay(),
                                               minimum_interest=CreditCard.pay(),Status_BC="True",usage=CreditCard.usage)

    # Act
    created_account = account.select().where(account.id == account.id).get()
    # Assert
    assert account.id == created_account.id
    assert account.user == created_account.user
    assert account.card == created_account.card
    assert account.Balance == created_account.Balance
    assert account.limit_date == created_account.limit_date
    assert account.credit_limit == created_account.credit_limit
    assert account.remaining_credit == created_account.remaining_credit
    assert account.minimum == created_account.minimum
    assert account.minimum_interest == created_account.minimum_interest
    assert account.Status_BC == created_account.Status_BC
    assert account.usage == created_account.usage

    # Delete test instances
    created_account.delete_instance()
import os
import pytest
from iugu import Iugu

@pytest.fixture
def token() -> str:

    if not 'IUGU_TOKEN' in os.environ:
        raise EnvironmentError('IUGU_TOKEN não está definido')

    return os.environ.get('IUGU_TOKEN')

def test_customer_create(token):

    iugu = Iugu(token)

    test_customer = {
        'email': 'vindiesel@silva.com',
        'name': 'Vin Diesel da Silva',
    }

    created_customer = iugu.customer.create(**test_customer)

    assert created_customer.get('email') == test_customer.get('email')
    assert created_customer.get('name')  == test_customer.get('name')

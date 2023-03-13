import pytest

@pytest.fixture
def set_up():
    print('\n__Start test__')
    yield
    print('__Finish test__')


@pytest.fixture
def data():
    street = 'Тестовая линия'
    house_numbers = '1'
    name = 'Александр'
    number_phone = '1111111111'
    return {"street": street, "house_numbers": house_numbers, "name": name, "number_phone": number_phone }
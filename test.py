from classes import Category, Product
import pytest


@pytest.fixture
def Category_electronics():
    return Category('Электроника',
                    'Компоненты, необходимые для работоспособности разных электрических приборов',
                    ['Батарея', 'Лампочка', 'Микросхема'])

def test_init1(Category_electronics):
    assert Category_electronics.title == 'Электроника'
    assert Category_electronics.descriptions == 'Компоненты, необходимые для работоспособности разных электрических приборов'
    assert Category_electronics.products == ['Батарея', 'Лампочка', 'Микросхема']
    assert Category_electronics.total_category == 1
    assert Category_electronics.total_unique_product == 3

@pytest.fixture
def Product_Battery():
    return Product('Батарея', 'Автономный источник постоянного тока',100, 200)


def test_init2(Product_Battery):
    assert Product_Battery.title == 'Батарея'
    assert Product_Battery.descriptions == 'Автономный источник постоянного тока'
    assert Product_Battery.price == 100
    assert Product_Battery.quantity == 200

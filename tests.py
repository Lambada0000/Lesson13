from class_Category import Category
from class_Product import Product, Smartphone, LawnGrass
import pytest


@pytest.fixture
def Category_electronics():
    return Category('Электроника',
                    'Компоненты, необходимые для работоспособности разных электрических приборов',
                    ['Батарея', 'Лампочка', 'Микросхема'])


def test_init1(Category_electronics):
    assert Category_electronics.title == 'Электроника'
    assert Category_electronics.descriptions == ('Компоненты, необходимые для работоспособности разных электрических '
                                                 'приборов')
    assert Category_electronics.products == ['Батарея', 'Лампочка', 'Микросхема']
    assert Category_electronics.total_category == 1
    assert Category_electronics.total_unique_product == 3


@pytest.fixture
def Product_Battery():
    return Product('Батарея', 'Автономный источник постоянного тока', 100, 200)


def test_init2(Product_Battery):
    assert Product_Battery.title == 'Батарея'
    assert Product_Battery.descriptions == 'Автономный источник постоянного тока'
    assert Product_Battery.price == 100
    assert Product_Battery.quantity == 200


@pytest.fixture
def Product_Smartphone():
    return Smartphone('Iphone 15 Pro Max',
                      'Titanium design, ceramic shield front, textured matte glass back',
                      120000,
                      100,
                      'A17 Pro chip, new 6‑core CPU with 2 performance and 4 efficiency cores, new 6‑core GPU, '
                      'new 16‑core Neural Engine',
                      'Pro Max',
                      512,
                      'Black Titanium')


def test_init3(Product_Smartphone):
    assert Product_Smartphone.title == 'Iphone 15 Pro Max'
    assert Product_Smartphone.descriptions == 'Titanium design, ceramic shield front, textured matte glass back'
    assert Product_Smartphone.price == 120000
    assert Product_Smartphone.quantity == 100
    assert Product_Smartphone.efficiency == ('A17 Pro chip, new 6‑core CPU with 2 performance and 4 efficiency cores, '
                                             'new 6‑core GPU, new 16‑core Neural Engine')
    assert Product_Smartphone.model == 'Pro Max'
    assert Product_Smartphone.memory == 512
    assert Product_Smartphone.color == 'Black Titanium'

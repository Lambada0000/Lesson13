from classes import Category, Product
import pytest


@pytest.fixture
def Category_Ponshiki():
    return Category('Пончики', 'Очень вкусные, но вредные', ['Клубничные', 'Ванильные', 'Шоколадные'])


def test_init1(Category_Ponshiki):
    assert Category_Ponshiki.title == 'Пончики'
    assert Category_Ponshiki.descritions == 'Очень вкусные, но вредные'
    assert Category_Ponshiki.products == ['Клубничные', 'Ванильные', 'Шоколадные']
    assert Category_Ponshiki.total_category == 3
    assert Category_Ponshiki.total_unique_product == 10


@pytest.fixture
def Product_Choco():
    return Product('Шоколадные пончики', 'Шоколадная начинка!', 89.99, 57)


def test_init2(Product_Choco):
    assert Product_Choco.title == 'Шоколадные пончики'
    assert Product_Choco.descritions == 'Шоколадная начинка!'
    assert Product_Choco.pay == 89.99
    assert Product_Choco.quantity == 57
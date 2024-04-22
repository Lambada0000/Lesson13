from abc import ABC, abstractmethod


class Base_Product(ABC):  # 1 задание
    """
    Абстрактный базовый класс, отображающий некоторый общий функционал его дочерних классов
    """

    @abstractmethod
    def __init__(self):
        pass

    def __add__(self, other):
        pass


class MixinLog:  # 2 задание
    """
    Миксин для вывода всей информации о созданном объекте
    """
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__.items()})"


class Product(Base_Product, MixinLog):
    title: str         # Название товара
    descriptions: str  # Описание товара
    price: float       # Цена товара
    quantity: int      # Количество в наличии

    def __init__(self, title, descriptions, price, quantity):
        super().__init__()
        self.title = title
        self.descriptions = descriptions
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.title}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.quantity * self.__price + other.quantity * other.__price

    @classmethod
    def create_product(cls, title, descriptions, price, quantity):
        """
        отразил создание товара и возвращение объекта,
        который можно добавлять в список товаров
        """
        if title in cls.title:
            cls.quantity += quantity
        else:
            return cls(title, descriptions, price, quantity)

    @property
    def new_price(self):
        return self.__price

    @new_price.setter
    def new_price(self, price):
        if self.__price >= price > 0:
            print('Вы действительно хотите понизить цену? (y/n):')
            if input('y'):
                self.__price = price
            if input('n'):
                print('Введите цену заново')
                return
            else:
                print('Попробуйте еще раз')
        if price > self.__price:
            self.__price = price
        if price < 0:
            print('Введите корректную цену')


class Smartphone(Product, Base_Product, MixinLog):
    efficiency = str  # Производительность
    model = str       # Модель
    memory = int      # Емкость внутренней памяти
    color = str       # Цвет

    def __init__(self, title, descriptions, price, quantity, efficiency, model, memory, color):  # 1 задание
        super().__init__(title, descriptions, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.quantity * self.__price + other.quantity * other.__price
        raise ValueError('Продукты принадлежат разным классам')


class LawnGrass(Product, Base_Product, MixinLog):
    country: str  # Страна - производитель
    period: int   # Срок прорастания
    color: str    # Цвет
    def __init__(self, title, descriptions, price, quantity, country, period, color):  # 1 задание
        super().__init__(title, descriptions, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.quantity * self.__price + other.quantity * other.__price
        raise ValueError('Продукты принадлежат разным классам')

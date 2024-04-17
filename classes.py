class Category:
    title: str
    descriptions: str
    products: list
    all_categories = []
    total_category: int
    total_unique_product: int

    def __init__(self, title, descriptions, products):
        self.title = title
        self.descriptions = descriptions
        self.__products = products
        self.all_categories.append(self)
        self.total_category = 0
        self.total_unique_product = 0

        for category in self.all_categories:
            self.total_category += 1
            for _ in category.__products:
                self.total_unique_product += 1

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.title}, количество продуктов: {self.__len__()} шт.'

    def new_product(self, product):  # 3 задание
        if isinstance(product, Product):
            self.total_unique_product += 1
            return self.__products.append(product)
        raise ValueError('Продукт не соответствует классу')

    @property
    def list_products(self):
        """отразил метод добавления геттера"""
        output = ''
        for product in self.__products:
            output = f'{product.name}, {product.pay} руб. Остаток: {product.quantity}\n'
        return output


class Product:
    title: str
    descriptions: str
    price: float
    quantity: int

    def __init__(self, title, descriptions, price, quantity):
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


class Product_Iterator(Category):  # Доп задание

    def __init__(self, title):
        self.title = title

    def __iter__(self):
        return self

    def __next__(self):
        for product in self.products:
            return product


class Smartphone(Product):
    efficiency = str
    model = str
    memory = int
    color = str

    def __init__(self, title, descriptions, price, quantity, efficiency, model, memory, color):  # 1 задание
        super().__init__(title, descriptions, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):  # 2 задание
        if isinstance(other, Smartphone):
            return self.quantity * self.__price + other.quantity * other.__price
        raise ValueError('Продукты принадлежат разным классам')


class LawnGrass(Product):
    def __init__(self, title, descriptions, price, quantity, country, period, color):  # 1 задание
        super().__init__(title, descriptions, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __add__(self, other):  # 2 задание
        if isinstance(other, LawnGrass):
            return self.quantity * self.__price + other.quantity * other.__price
        raise ValueError('Продукты принадлежат разным классам')

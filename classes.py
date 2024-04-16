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
        self.__products = products  # сделал список товаров приватным атрибутом
        self.all_categories.append(self)
        self.total_category = 0
        self.total_unique_product = 0

        for category in self.all_categories:
            self.total_category += 1
            for _ in category.products:
                self.total_unique_product += 1

    def __len__(self):  # Подсчитывает количество продуктов на складе
        return len(self.__products)

    def __str__(self):  # 1 задание
        return f'{self.title}, количество продуктов: {self.__len__()} шт.'

    def new_product(self, product):
        """отразил метод добавления товара в список"""
        self.total_unique_product += 1
        return self.__products.append(product)

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

    def __str__(self):  # 1 задание
        return f'{self.title}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):  # 2 задание
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

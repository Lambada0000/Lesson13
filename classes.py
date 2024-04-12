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
    pay: float
    quantity: int

    def __init__(self, title, descriptions, price, quantity):
        self.title = title
        self.descriptions = descriptions
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(self, title, descriptions, price, quantity):
        """
        отразил создание товара и возвращение объекта,
        который можно добавлять в список товаров
        """
        if title in self.title:
            self.quantity += quantity
        else:
            return title, descriptions, price, quantity

    # @price.setter
    # def price(self, new_price):
    #     """
    #     реализовал метод для проверки введенной цены
    #     """
    #     if new_price <= 0:
    #         print('Цена введена некорректно')
    #     else:
    #         self.price = new_price

    @price.setter
    def price(self, new_price):
        if new_price <= self.price:
            print('Вы действительно хотите понизить цену? (y/n):')
            if int('y'):
                self.price = new_price
            else:
                print('Попробуйте еще раз')
        else:
            self.price = new_price

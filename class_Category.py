from class_Product import Product, Smartphone, LawnGrass


class Category:
    title: str                 # Название категории
    descriptions: str          # Описание категории
    products: list             # Список продуктов категории
    all_categories = []        # Список всех категорий
    total_category: int        # Общее количество категорий
    total_unique_product: int  # Общее количество товаров

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

    def new_product(self, product):
        '''
        Сначала проверяются все условия для добавления продукта
        '''
        if not isinstance(product, Product):
            raise TypeError('Продукт не соответствует классу')
        elif product.quantity == 0:
            raise ValueError('Продукт с нулевым количеством не может быть добавлен')
        self.total_unique_product += 1
        return self.__products.append(product)

    def average_price(self):
        try:
            total_price = 0
            for product in self.__products:
                total_price += product.price
                average_price = total_price/len(self.__products)
                return average_price
        except ZeroDivisionError:
            return 0

    @property
    def list_products(self):
        """отразил метод добавления геттера"""
        output = ''
        for product in self.__products:
            output = f'{product.title}, {product.price} руб. Остаток: {product.quantity}\n'
        return output


class Product_Iterator(Category):
    def __init__(self, title, descriptions, products):
        super().__init__(title, descriptions, products)
        self.title = title

    def __iter__(self):
        return self

    def __next__(self):
        for product in self.products:
            return product

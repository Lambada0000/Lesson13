
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
        self.products = products
        self.all_categories.append(self)
        self.total_category = 0
        self.total_unique_product = 0

        for category in self.all_categories:
            self.total_category += 1
            for _ in category.products:
                self.total_unique_product += 1


class Product:
    title: str
    descriptions: str
    pay: float
    quantity: int

    def __init__(self, title, descriptions, pay, quantity):
        self.title = title
        self.descriptions = descriptions
        self.pay = float(pay)
        self.quantity = quantity

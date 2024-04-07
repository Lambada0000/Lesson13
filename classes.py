class Category:
    title: str
    descritions: str
    products: list

    def __init__(self, title, descriptoins, products):
        self.title = title
        self.descritions = descriptoins
        self.products = products
        self.total_category = len(products)
        self.total_unique_product = 10


class Product:
    title: str
    descritions: str
    pay: float
    quantity: int

    def __init__(self, title, descriptions, pay, quantity):
        self.title = title
        self.descritions = descriptions
        self.pay = float(pay)
        self.quantity = quantity
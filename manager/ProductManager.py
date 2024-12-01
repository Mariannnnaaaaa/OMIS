from StandardProductManager import StandardProductManager
from model.Product import Product

class ProductManager(StandardProductManager):
    def __init__(self):
        self.products = []

    def display_products(self):
        pass

    def add_to_favorites(self, product: Product):
        pass

    def add_to_basket(self, product: Product):
        pass
from StandardPurchaseHistoryManager import StandardPurchaseHistoryManager
from model.Product import Product

class PurchaseHistoryManager(StandardPurchaseHistoryManager):
    def __init__(self):
        self.products = []

    def display_products(self):
        pass

    def load_product(self, product: Product):
        pass
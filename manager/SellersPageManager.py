from StandardSellersPageManager import StandardSellersPageManager
from model.Product import Product
from model.User import User

class SellersPageManager(StandardSellersPageManager):
    def __init__(self, seller: User):
        self.products = []
        self.__seller = seller

    def display_products(self):
        pass

    def view_sale_history(self, product: Product):
        pass

    def add_product(self, product: Product):
        pass

    def view_sales_statistics(self):
        pass
from StandardFavoritesManager import StandardFavoritesManager
from model.Product import Product

class FavoritesManager(StandardFavoritesManager):
    def __init__(self):
        self.products = []

    def display_products(self):
        pass

    def remove_from_favorites(self, product: Product):
        pass
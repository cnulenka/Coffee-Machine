from models.Outlet import Outlet


class VendingMachine:
    def __init__(self):
        self._outlets = Outlet()
        self._ingredients_quantity_map = {}
        self._beverages = {}

    def set_num_outlets(self, num_outlets):
        self._outlets.set_count(num_outlets)

    def set_ingredients_quantity(self, ingredients_quantity_map):
        self._ingredients_quantity_map = ingredients_quantity_map

    def set_beverages(self, beverages):
        self._beverages = beverages

    def get_ingredients_quantity(self):
        return self._ingredients_quantity_map

    def get_beverages(self):
        return self._beverages

    def get_num_outlets(self):
        return self._outlets.get_count()

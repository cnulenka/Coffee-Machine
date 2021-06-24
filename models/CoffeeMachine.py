class CoffeeMachine:
    
    def __init__(self):
        self._num_outlets = 0
        self._ingredients_quantity_map = {}
        self._beverages = {}

    def set_num_outlets(self, num_outlets):
        self._num_outlets = num_outlets
    
    def set_ingredients_quantity(self, ingredients_quantity_map):
        self._ingredients_quantity_map = ingredients_quantity_map
    
    def set_beverages(self, beverages):
        self._beverages = beverages
    
    def get_num_outlets(self, num_outlets):
        return self._num_outlets
    
    def get_ingredients_quantity(self, ingredients_quantity_map):
        return self._ingredients_quantity_map
    
    def get_beverages(self, beverages):
        return self._beverages
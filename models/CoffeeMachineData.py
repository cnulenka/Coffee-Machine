class CoffeeMachineData:
    
    def __init__(self, input_json: dict = None):
        if input_json:
            self._num_outlets = input_json["machine"]["outlets"]["count_n"]
            self._ingredients_quantity_map = input_json["machine"]["total_items_quantity"]
            self._beverages = input_json["machine"]["beverages"]
        else:
            self._num_outlets = 0
            self._ingredients_quantity_map = {}
            self._beverages = {}
    
    def set_num_outlets(self, num_outlets):
        self._num_outlets = num_outlets
    
    def set_ingredients_quantity(self, ingredients_quantity_map):
        self._ingredients_quantity_map = ingredients_quantity_map
    
    def set_beverages(self, beverages):
        self._beverages = beverages
    
    def get_ingredients_quantity(self):
        return self._ingredients_quantity_map
    
    def get_beverages(self):
        return self._beverages

    def get_num_outlets(self):
        return self._num_outlets
    
    def get_ingredients_quantity(self):
        return self._ingredients_quantity_map
    
    def get_beverages(self):
        return self._beverages
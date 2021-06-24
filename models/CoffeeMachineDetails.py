class CoffeeMachineDetails:
    
    def __init__(self, input_json: dict):
        self._num_outlets = input_json["machine"]["outlets"]["count_n"]
        self._ingredients_quantity_map = input_json["total_items_quantity"]
        self._beverages = input_json["beverages"]
    
    def get_num_outlets(self):
        return self._num_outlets
    
    def get_ingredients_quantity(self):
        return self._ingredients_quantity_map
    
    def get_beverages(self):
        return self._beverages
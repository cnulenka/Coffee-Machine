from utils.Results import Results
from services.ValidateInputService import ValidateInputService
from models.VendingMachine import VendingMachine

import jsonschema

class CoffeeMachineData(VendingMachine):
    
    def __init__(self):
        super().__init__()
    
    def validate_full_input_data(self, input_json: dict) -> Results:
        results = Results()
        try:
            ValidateInputService.validate_coffee_machine_full_input(input_json)
        except jsonschema.exceptions.ValidationError:
            results.errors.append("Wrong Input JSON format. Please check README for reference")
        try:
            self._outlets.set_count(input_json["machine"]["outlets"]["count_n"])
        except KeyError:
            missing_keys = '["machine"]["outlets"]["count_n"]'
            results.errors.append(f"Please check input json, missing required keys({missing_keys})")
        
        try:
            self._ingredients_quantity_map = input_json["machine"]["total_items_quantity"]
        except KeyError:
            missing_keys = '["machine"]["total_items_quantity"]'
            results.errors.append(f"Please check input json, missing required keys({missing_keys})")
        
        try:
            self._beverages = input_json["machine"]["beverages"]
        except KeyError:
            missing_keys = '["machine"]["beverages"]'
            results.errors.append(f"Please check input json, missing required keys({missing_keys})")
        
        return results
    
    def set_data(self, input_json: dict):
        results = self.validate_full_input_data(input_json)

        if len(results.errors) == 0:
            self._outlets.set_count(input_json["machine"]["outlets"]["count_n"])
            self._ingredients_quantity_map = input_json["machine"]["total_items_quantity"]
            self._beverages = input_json["machine"]["beverages"]
        
        return results
    
    def clear_data(self):
        self._num_outlets = 0
        self._ingredients_quantity_map.clear()
        self._beverages.clear()
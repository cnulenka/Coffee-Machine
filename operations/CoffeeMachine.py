from models.InventoryManager import InventoryManager
from models.CoffeeMachineDetails import CoffeeMachineDetails
from models.Beverage import Beverage
from models.SingletonMeta import SingletonMeta
from .BeverageMakerTask import BeverageMakerTask


class CoffeeMachine(metaclass=SingletonMeta):

    def __init__(self, input_json):
        self._input_json = input_json
        self._details = CoffeeMachineDetails(input_json)
        self._inventory_manager = None
    
    def process(self):
        self._inventory_manager = InventoryManager()
        ingredients = self._details.get_ingredients_quantity()

        for ingredient, quantity in ingredients.items():
            self._inventory_manager.add_ingredients_to_inventory(ingredient, quantity)
        
        beverages = self._details.get_beverages()
        
        for beverage_name, beverage_composition in beverages.items():
            beverage = Beverage(beverage_name, beverage_composition)
            self.add_beverage_request(beverage) 
    
    def add_beverage_request(self, beverage: Beverage):
        task = BeverageMakerTask(beverage)
        task.run()

    def stop_machine(self):
        #stop thread executor
        pass

    def reset(self):
        self.stop_machine()
        self._inventory_manager.clear_inventory()
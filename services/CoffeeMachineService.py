from models.InventoryManager import InventoryManager
from models.CoffeeMachineData import CoffeeMachineData
from models.Beverage import Beverage
from models.SingletonMeta import SingletonMeta
from .BeverageMakerTask import BeverageMakerTask

import threading


class CoffeeMachineService(metaclass=SingletonMeta):

    def __init__(self, input_json):
        self._input_json = input_json
        self._details = CoffeeMachineData(input_json)
        self._inventory_manager = InventoryManager()
        self._threads = list()
    
    def add_ingredients_to_inventory(self, ingredients_update_info):
        pass
    
    def process_order(self):
        ingredients = self._details.get_ingredients_quantity()

        for ingredient, quantity in ingredients.items():
            self._inventory_manager.add_ingredients_to_inventory(ingredient, quantity)
        
        beverages = self._details.get_beverages()
        
        for beverage_name, beverage_composition in beverages.items():
            beverage = Beverage(beverage_name, beverage_composition)
            task_thread = threading.Thread(target=self.add_beverage_request, args=(beverage,))
            self._threads.append(task_thread)
            task_thread.start()
        
        for index, thread in enumerate(self._threads):
            #add each thread to main thread
            #print("Main    : before joining thread {}.".format(index))
            thread.join()
            #print("Main    : thread {} done".format(index))
    
    def add_beverage_request(self, beverage: Beverage):
        task = BeverageMakerTask(beverage)
        task.run()

    def reset(self):
        self._inventory_manager.clear_inventory()
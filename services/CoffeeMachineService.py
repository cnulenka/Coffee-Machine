from models.InventoryManager import InventoryManager
from models.CoffeeMachineData import CoffeeMachineData
from models.Beverage import Beverage
from models.SingletonMeta import SingletonMeta
from .BeverageMakerService import BeverageMakerService
from utils.Utils import *

import threading


class CoffeeMachineService(metaclass=SingletonMeta):

    def __init__(self, input_json):
        self._input_json = input_json
        self._data = CoffeeMachineData(input_json)
        self.setup()
        self.add_ingredients_to_inventory()
    
    def __init__(self, num_outlets):
        self._num_outlets = num_outlets
        self._data = CoffeeMachineData()
        self._data.set_num_outlets(num_outlets)
        self.setup()
    
    def setup(self):
        self._inventory_manager = InventoryManager()
        self._threads = list()
    
    def add_ingredients_to_inventory(self, ingredients_update_info):
        ingredients = []
        if ingredients_update_info  == None:
            ingredients = self._data.get_ingredients_quantity()
        else:
            ingredients = ingredients_update_info["total_items_quantity"]
        
        for ingredient, quantity in ingredients.items():
            self._inventory_manager.add_ingredients_to_inventory(ingredient, quantity)
    
    def process_order(self, beverages_order_info):
        orders = []
        if beverages_order_info  == None:
            orders = self._data.get_beverages()
        else:
            orders = beverages_order_info["beverages"]
        
        self.threaded_order_dispatcher(orders)
    
    def threaded_order_dispatcher(self, orders):
        '''
            spawn n threads for n beverages.
        '''
        for beverage_name, beverage_composition in orders.items():
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
        service = BeverageMakerService(beverage)
        service.execute()

    def reset(self):
        self._inventory_manager.clear_inventory()
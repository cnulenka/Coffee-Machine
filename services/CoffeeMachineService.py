from models.InventoryManager import InventoryManager
from models.CoffeeMachineData import CoffeeMachineData
from models.Beverage import Beverage
from .BeverageMakerService import BeverageMakerService
from models.SingletonMeta import SingletonCoffeeServiceMeta
from utils.Results import Results
import pdb
import threading
from utils.Logger import Logger

class CoffeeMachineService(metaclass=SingletonCoffeeServiceMeta):

    def __init__(self, input_json: dict = None, num_outlets: int = None):
        #pdb.set_trace()
        self._results = Results()
        #pdb.set_trace()
        self._inventory_manager = InventoryManager()
        #pdb.set_trace()
        self._threads = list()
        self._data = CoffeeMachineData()
        #pdb.set_trace()
        if input_json and not num_outlets:
            #pdb.set_trace()
            input_validation_results = self._data.set_data(input_json)
            self._results.append_results(input_validation_results)
            #pdb.set_trace()
            self.add_ingredients_to_inventory()
            #pdb.set_trace()
        elif num_outlets and not input_json:
            self._data.set_num_outlets(num_outlets)
    
    def add_ingredients_to_inventory(self, ingredients_update_info = None):
        #pdb.set_trace()
        ingredients = []
        if ingredients_update_info  == None:
            ingredients = self._data.get_ingredients_quantity()
        else:
            ingredients = ingredients_update_info["total_items_quantity"]
        
        for ingredient, quantity in ingredients.items():
            self._inventory_manager.add_ingredients_to_inventory(ingredient, quantity)
    
    def validate_input_data(self, json):
        return self._data.validate_input_data(json)

    def process_order(self, beverages_order_info = None) -> Results:
        orders = []
        #pdb.set_trace()
        if beverages_order_info  == None:
            #pdb.set_trace()
            orders = self._data.get_beverages()
            #pdb.set_trace()
        else:
            orders = beverages_order_info["beverages"]
        Logger.get_logger().info("==========================================================")
        self.threaded_order_dispatcher(orders)
        Logger.get_logger().info("==========================================================")
        inventory_check_results = self.low_quantity_indicator_message()
        self._results.append_results(inventory_check_results)
        #pdb.set_trace()
        return self._results
    
    def threaded_order_dispatcher(self, orders):
        '''
            spawn n threads for n beverages.
        '''
        self._threads = []
        for beverage_name, beverage_composition in orders.items():
            beverage = Beverage(beverage_name, beverage_composition)
            task_thread = threading.Thread(target=self.add_beverage_request, args=(beverage,))
            self._threads.append(task_thread)
            task_thread.start()

        for index, thread in enumerate(self._threads):
            #add each thread to main thread
            Logger.get_logger().info("Main    : before joining thread {}.".format(index))
            thread.join()
            Logger.get_logger().info("Main    : thread {} done".format(index))
    
    def add_beverage_request(self, beverage: Beverage):
        service = BeverageMakerService(beverage)
        results = service.execute()
        self._results.append_results(results)
    
    def low_quantity_indicator(self) -> list:
        return self._inventory_manager.check_for_low_quantity()

    def low_quantity_indicator_message(self) -> Results:
        results = Results()
        low_quantity_ingredients = self.low_quantity_indicator()
        if len(low_quantity_ingredients) > 0:
            low_quantity_warning = "\nBelow ingredients are running low, please refill!!\n"
            for ingredient in low_quantity_ingredients:
                quantity_left = ingredient["quantity"]
                low_quantity_warning += ingredient["name"] + f" {quantity_left}ml left" + "\n"
            results.warnings.append(low_quantity_warning)
        
        return results
    
    def get_invetory_status(self) -> dict:
        return self._inventory_manager.get_inventory_status()
    
    def get_num_outlets(self):
        return self._data.get_num_outlets()
    
    def get_num_orders(self):
        return len(self._data.get_beverages())
    
    def reset_results(self):
        self._results.reset_results()
    
    def set_machine_data(self, input_json):
        self._data.set_data(input_json)
    
    def reset_service(self):
        self.reset_results()
        self._inventory_manager.clear_inventory()
        self._data.clear_data()
import pdb
import threading

import jsonschema

from models.Beverage import Beverage
from models.CoffeeMachineData import CoffeeMachineData
from models.InventoryManager import InventoryManager
from models.SingletonMeta import SingletonVendingServiceMeta
from utils.Logger import logger
from utils.Results import Results

from .BeverageMakerService import BeverageMakerService


class CoffeeMachineService(metaclass=SingletonVendingServiceMeta):

    """
        Most important class of project. Represents the singleton 
        coffee machine service i.e the operations of a coffee machine.

        Provides service like updating invetory and order placement.
        Also has methods to provide low quanity warnings.

        Behaves as a FACADE for inventory, CoffeeMachineData, exposes
        apis useful for testing and to provide information/warnings
        to users.
    """

    def __init__(self, input_json: dict = None, num_outlets: int = None):

        self._inventory_manager = InventoryManager()
        self._coffee_machine_data = CoffeeMachineData()
        self._threads = list()
        self._results = Results()

        if input_json and not num_outlets:

            input_validation_results = self._coffee_machine_data.set_data(input_json)
            self._results.append_results(input_validation_results)

            input_validation_results = self.add_ingredients_to_inventory()
            self._results.append_results(input_validation_results)

        elif num_outlets and not input_json:
            self._coffee_machine_data.set_num_outlets(num_outlets)

    def add_ingredients_to_inventory(self, ingredients_update_info=None):

        """
            Update ingredients in inventory.
            Verify the input json for input consistency.
        """

        ingredients = []
        if ingredients_update_info == None:
            ingredients = self._coffee_machine_data.get_ingredients_quantity()
        else:
            input_validation_results = self.validate_ingredients_input_data(
                ingredients_update_info
            )
            self._results.append_results(input_validation_results)
            try:
                ingredients = ingredients_update_info["total_items_quantity"]
            except KeyError as e:
                print(e)
                self._results.errors.append(
                    "Input json does not have total_items_quantity key, Please check Input."
                )
                return self._results

        for ingredient, quantity in ingredients.items():
            results = self._inventory_manager.add_ingredients_to_inventory(
                ingredient, quantity
            )
            if len(results.errors) > 0:
                self._results.append_results(results)
                return self._results

        return self._results

    def process_order(self, beverages_order_info=None) -> Results:
        """
            Processes the coming orders and returns information
            where ordered item could be prepared or not.
        """
        orders = []

        if beverages_order_info == None:
            orders = self._coffee_machine_data.get_beverages()
        else:
            input_validation_results = self.validate_beverages_input_data(
                beverages_order_info
            )
            self._results.append_results(input_validation_results)
            try:
                orders = beverages_order_info["beverages"]
            except KeyError as e:
                print(e)
                return self._results

        logger.info("==========================================================")
        self.threaded_order_dispatcher(orders)
        logger.info("==========================================================")
        inventory_check_results = self.low_quantity_indicator_message()
        self._results.append_results(inventory_check_results)

        return self._results

    def threaded_order_dispatcher(self, orders):
        """
            spawn n threads for n beverages. Log
            the threads info for better debuggability.
        """
        self._threads = []
        for beverage_name, beverage_composition in orders.items():
            beverage = Beverage(beverage_name, beverage_composition)
            task_thread = threading.Thread(
                target=self.add_beverage_request, args=(beverage,)
            )
            self._threads.append(task_thread)
            task_thread.start()

        for index, thread in enumerate(self._threads):
            # add each thread to main thread
            logger.info("Main    : before joining thread {}.".format(index))
            thread.join()
            logger.info("Main    : thread {} done".format(index))

    def add_beverage_request(self, beverage: Beverage):
        """
            Use BeverageMakerService to serve/complete
            the order as a atomic threaded task.
        """
        service = BeverageMakerService(beverage)
        results = service.make_beverage()
        self._results.append_results(results)

    def reset_results(self):
        self._results.reset_results()

    def get_results(self):
        return self._results

    def reset_service(self):
        self.reset_results()
        self._inventory_manager.clear_inventory()
        self._coffee_machine_data.clear_data()

    """
    Facade for InventoryManager

    """

    def low_quantity_indicator_message(self) -> Results:
        """
            Returns name of the ingredients running low.
        """
        results = Results()
        low_quantity_ingredients = self.low_quantity_indicator()
        if len(low_quantity_ingredients) > 0:
            low_quantity_warning = (
                "\nBelow ingredients are running low, please refill!!\n"
            )
            for ingredient in low_quantity_ingredients:
                quantity_left = ingredient["quantity"]
                low_quantity_warning += (
                    ingredient["name"] + f" {quantity_left}ml left" + "\n"
                )
            results.warnings.append(low_quantity_warning)

        return results

    def low_quantity_indicator(self) -> list:
        return self._inventory_manager.check_for_low_quantity()

    def get_invetory_status(self) -> dict:
        return self._inventory_manager.get_inventory_status()

    """
    Facade for CoffeeMachineData
    """

    def get_num_outlets(self):
        return self._coffee_machine_data.get_num_outlets()

    def get_num_orders(self):
        return len(self._coffee_machine_data.get_beverages())

    def set_machine_data(self, input_json):
        self._coffee_machine_data.set_data(input_json)

    """
        Input validators
    """

    def validate_full_input_data(self, json):
        return self._coffee_machine_data.validate_full_input_data(json)

    def validate_ingredients_input_data(self, ingredients_input: dict) -> Results:
        return self._coffee_machine_data.validate_ingredients_input_data(
            ingredients_input
        )

    def validate_beverages_input_data(self, beverages_input: dict) -> Results:
        return self._coffee_machine_data.validate_beverages_input_data(beverages_input)

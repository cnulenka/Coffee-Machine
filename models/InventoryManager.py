import pdb
from threading import Lock

from utils.constants import LOW_QUANTITY_WARNING_LIMIT
from utils.Logger import logger
from utils.Results import Results

from .Beverage import Beverage
from .SingletonMeta import SingletonInventoryManagerMeta


class InventoryManager(metaclass=SingletonInventoryManagerMeta):
    def __init__(self) -> None:
        self._inventory = {}
        self._lock = Lock()

    def validate_order_ingredients_availability(self, beverage: Beverage):
        results = Results()
        required_compostion = beverage.get_composition()
        is_possible = True
        for ingredient in required_compostion:
            ingredient_inventory_quantity = self._inventory.get(ingredient, 0)
            if ingredient_inventory_quantity == 0:
                results.info.append(
                    f"{beverage.get_name()} cannot be prepared because {ingredient} is not available."
                )
                is_possible = False
                break
            elif required_compostion[ingredient] > ingredient_inventory_quantity:
                results.info.append(
                    f"{beverage.get_name()} cannot be prepared because {ingredient} is not sufficient"
                )
                is_possible = False
                break

        return is_possible, results

    def produce_beverage(self, beverage: Beverage):
        logger.info("Thread {} about to lock".format(beverage.get_name()))
        self._lock.acquire()
        logger.info("Thread {} lock acquired".format(beverage.get_name()))
        is_possible, results = self.validate_order_ingredients_availability(beverage)
        required_compostion = beverage.get_composition()
        if is_possible:
            for ingredient in required_compostion:
                ingredient_inventory_quantity = self._inventory.get(ingredient, 0)
                self._inventory[ingredient] = (
                    ingredient_inventory_quantity - required_compostion[ingredient]
                )
            results.info.append(f"{beverage.get_name()} is prepared.")
        self._lock.release()
        logger.info("Thread {} after release".format(beverage.get_name()))
        return results

    def add_ingredients_to_inventory(self, ingredient: str, quantity: float):
        ingredient_inventory_quantity = self._inventory.get(ingredient, 0)
        self._inventory[ingredient] = ingredient_inventory_quantity + quantity

    def check_for_low_quantity(self):
        ingredients_with_low_quantity = []
        for ingredient, quantity in self._inventory.items():
            if quantity <= LOW_QUANTITY_WARNING_LIMIT:
                ingredients_with_low_quantity.append(
                    {"name": ingredient, "quantity": quantity}
                )

        return ingredients_with_low_quantity

    def get_inventory_status(self):
        status = []
        for ingredient, quantity in self._inventory.items():
            status.append({"name": ingredient, "quantity": quantity})
        return status

    def clear_inventory(self):
        self._inventory.clear()

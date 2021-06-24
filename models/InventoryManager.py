from .Beverage import Beverage
from .SingletonMeta import SingletonMeta

from threading import Lock

class InventoryManager(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._inventory = {}
        self._lock = Lock()
    
    def check_and_update_inventory(self, beverage: Beverage):
        print("Thread {} about to lock".format(beverage.get_name()))
        self._lock.acquire()
        print("Thread {} lock acquired".format(beverage.get_name()))
        required_compostion = beverage.get_composition()
        is_possible = True
        for ingredient in required_compostion:
            ingredient_inventory_quantity= self._inventory.get(ingredient, 0)
            if ingredient_inventory_quantity == 0:
                print("{} cannot be prepared because {} is not available".format(beverage.get_name(), ingredient))
                is_possible = False
                break
            elif required_compostion[ingredient] > ingredient_inventory_quantity:
                print("{} cannot be prepared because {} is not sufficient".format(beverage.get_name(), ingredient))
                is_possible = False
                break
        
        if is_possible:
            for ingredient in required_compostion:
                ingredient_inventory_quantity= self._inventory.get(ingredient, 0)
                self._inventory[ingredient] = ingredient_inventory_quantity - required_compostion[ingredient]
        self._lock.release()
        print("Thread {} after release".format(beverage.get_name()))
        return is_possible


    def add_ingredients_to_inventory(self, ingredient: str, quantity: float):
        ingredient_inventory_quantity= self._inventory.get(ingredient, 0)
        self._inventory[ingredient] = ingredient_inventory_quantity + quantity


    def clear_inventory(self):
        self._inventory.clear()
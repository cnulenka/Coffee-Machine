import pdb
from threading import Lock

from utils.constants import LOW_QUANTITY_WARNING_LIMIT
from utils.Logger import logger
from utils.Results import Results

from .Beverage import Beverage
from .SingletonMeta import SingletonInventoryManagerMeta


class InventoryManager(metaclass=SingletonInventoryManagerMeta):

    '''
        InventoryManager is a singleton class, as each coffee
        machine should have only one inventory, hence on enitity
        to manage that shared resources.

        InventoryManager uses locks to handle orders coming in
        as multiple threads.

        Locks here help to maintain consistency in data.

        Inventory is initialised at the start of coffee machine,
        is added/update with data as request comes from user.

        Same instance is maintained through out one coffee machine
        session.
    '''

    def __init__(self) -> None:
        self._inventory : dict = {}
        self._lock = Lock()
    
    def add_ingredients_to_inventory(self, ingredient: str, quantity: float):
        '''
            populate the inventory, error handling to handle scenarios
            when input json has wrong input format.

            InventoryManager can be added with methods to handle quantites
            written in string which I guess is outside the scope of this
            assignment.
        '''
        results = Results()
        
        try:
            ingredient_inventory_quantity = self._inventory.get(ingredient, 0)
            self._inventory[ingredient] = ingredient_inventory_quantity + quantity
        except TypeError as e:
            results.errors.append("Quantity values in JSON should be integer not strings")
        
        return results

    def produce_beverage(self, beverage: Beverage):

        '''
            produce_beverage is crux of this application, it does the most
            important function i.e to check if a order is possible by using
            exisiting inventory ingredients quantity.

            If possible then decrease the required ingredients quantities from
            inventory and return success.

            Locks are used to maintain consistency of inventory data as inventory
            is a shared data.
        '''

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

    def check_for_low_quantity(self):
        
        '''
            method is used to raise warning incase
            ingredients are running low.

            called after every order request or inventory update
            resuest from user
        '''

        ingredients_with_low_quantity = []
        for ingredient, quantity in self._inventory.items():
            if quantity <= LOW_QUANTITY_WARNING_LIMIT:
                ingredients_with_low_quantity.append(
                    {"name": ingredient, "quantity": quantity}
                )

        return ingredients_with_low_quantity

    def get_inventory_status(self):
        '''
            returns a list with current quantity
            information of each ingredient
        '''
        status = []
        for ingredient, quantity in self._inventory.items():
            status.append({"name": ingredient, "quantity": quantity})
        return status

    def clear_inventory(self):
        self._inventory.clear()

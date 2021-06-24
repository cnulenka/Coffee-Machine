from models.Beverage import Beverage
from models.InventoryManager import InventoryManager

class BeverageMakerTask:

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
        self._inventory_manager = InventoryManager()
    
    def run(self):
        is_created = self._inventory_manager.check_and_update_inventory(self._beverage)
        if is_created:
            print("{} is prepared.".format(self._beverage.get_name))
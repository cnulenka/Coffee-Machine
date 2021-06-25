from models.Beverage import Beverage
from models.InventoryManager import InventoryManager
from utils.Utils import *
from utils.Constants import RESULTS

class BeverageMakerService:

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
        self._inventory_manager = InventoryManager()
    
    def execute(self) -> RESULTS:
        return self._inventory_manager.produce_beverage(self._beverage)
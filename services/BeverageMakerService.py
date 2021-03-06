from models.Beverage import Beverage
from models.InventoryManager import InventoryManager
from utils.Results import Results


class BeverageMakerService:

    """
        Represents a single atomic task with all
        required information to be needed
        for completing one thread of
        beverage order placement.
    """

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
        self._inventory_manager = InventoryManager()

    def make_beverage(self) -> Results:
        return self._inventory_manager.produce_beverage(self._beverage)

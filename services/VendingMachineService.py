from abc import ABC, abstractmethod

class VendingMachineService(ABC):

    @abstractmethod
    def process_order(self):
        pass
    
    @abstractmethod
    def add_ingredients_to_inventory(self):
        pass
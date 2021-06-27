from abc import ABC, abstractmethod


class VendingMachineService(ABC):

    """
        VendingMachineService abstract class
        represents the  basic and essential 
        operations done by any vending machine.

        It specifies certain must implement
        methods to child classes like
        CoffeeMachineService.

        Behaves a prototype for any kind
        of vending machine.

        Was added keeping in mind the extendibility
        of the product.

    """

    @abstractmethod
    def process_order(self):
        pass

    @abstractmethod
    def add_ingredients_to_inventory(self):
        pass


"""
    CANDIDATE NOTE:

    I could not use this parent class for CoffeeMachineService
    class as I was getting some errors with python for
    using singletone child class of this type.

    Owing to the time constraints for given project, i couln't
    explore and dig the real issue here. Had to move ahead and
    submit the project.

    This however doesn't affect the behavior of the project.
    This is only for a better design and extendibility.
"""

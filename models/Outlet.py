class Outlet:

    """
        Outlet class represents outlets in a 
        vending machine.

        It is a different class in favour of
        extensibility and Separatiion of Concern.
    """

    def __init__(self) -> None:
        self._num_outlets = 0

    def set_outlet_count(self, count):
        self._num_outlets = count

    def get_outlet_count(self):
        return self._num_outlets


"""
    CANDIDATE NOTE:
    
    May be in future we
    would like to have different type of
    outlets may be larger,smaller or
    may be each outlet is for different type of
    beverage.

    Vending Machine can have a list of
    different kind of outlets.
    
    Again Outlet can be a abstract class
    inherited by many type of outlets.
"""

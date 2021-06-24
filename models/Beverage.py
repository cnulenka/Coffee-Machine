class Beverage:
 
    def __init__(self, beverage_name: str, beverage_composition: dict):
        self._name = beverage_name
        self._composition = beverage_composition
    
    def get_name(self):
        return self._name
    
    def get_composition(self):
        return self._composition

class Beverage:

    '''
    Beverage class represents a beverage, which has a name
    and is made up of a list of ingredients.

    self._composition is a python dict with ingredient name as
    key and ingredient quantity as value
    '''

    def __init__(self, beverage_name: str, beverage_composition: dict):
        self._name: str = beverage_name
        self._composition: dict = beverage_composition

    def get_name(self):
        return self._name

    def get_composition(self):
        return self._composition


'''
CANDIDATE NOTE:

    one other idea here was to make a abstract Beverage class and inherit and
    create child classes of hot_coffee, black_coffee, hot_tea etc where each of
    them over ride get_composition and store the composition info with in class.

    So orders will be a list of Beverage objects having child class instances.

    But this would hard code the composition and types of Beverages, hence extensibility
    will be affected, but may be we can have a custom child class also where user
    can create any beverage object by setting name and composition.

    Same approach can be followed for Ingredients Class. I don't have a Ingredients class
    though. Each ingredient can have a different warning limit, hence get_warning_limit
    will be implemented differently. For example water is most used resource so that 
    can have a warning limit of 50% may be.

    -Shakti Prasad Lenka
'''
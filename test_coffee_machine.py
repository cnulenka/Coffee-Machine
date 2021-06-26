import unittest
import pdb
#pdb.set_trace()
from services.CoffeeMachineService import CoffeeMachineService
import json

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_4_outlets_success(self):
        input_json_file = open("input_json_1.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        coffee_service = CoffeeMachineService(input_json=input_json)
        results = coffee_service.process_order()

        assert(len(results.info) == 4)
        assert(len(results.warnings) == 1)
        assert(len(results.errors) == 0)
        assert(coffee_service.get_num_outlets() == 4)
        expected_inventory_status = [
            {'name': 'hot_water', 'quantity': 200},
            {'name': 'hot_milk', 'quantity': 0},
            {'name': 'ginger_syrup', 'quantity': 60},
            {'name': 'sugar_syrup', 'quantity': 40},
            {'name': 'tea_leaves_syrup', 'quantity': 40}
            ]
        self.assertListEqual(coffee_service.get_invetory_status(), expected_inventory_status)

        coffee_service.reset_service()

if __name__ == '__main__':
    #pdb.set_trace()
    unittest.main()
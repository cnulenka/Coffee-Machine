import unittest
import pdb
#pdb.set_trace()
from services.CoffeeMachineService import CoffeeMachineService
import json

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        self.coffee_service = CoffeeMachineService()
    
    def tearDown(self):
        pass
    
    def test_4_outlets_success(self):
        input_json_file = open("input_json_1.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert(len(results.info) == 4)
        assert(len(results.warnings) == 1)
        assert(len(results.errors) == 0)
        assert(self.coffee_service.get_num_orders() == 4)
        assert(self.coffee_service.get_num_outlets() == 4)
        assert(len(self.coffee_service.low_quantity_indicator()) == 3)
        expected_inventory_status = [
            {'name': 'hot_water', 'quantity': 200},
            {'name': 'hot_milk', 'quantity': 0},
            {'name': 'ginger_syrup', 'quantity': 60},
            {'name': 'sugar_syrup', 'quantity': 40},
            {'name': 'tea_leaves_syrup', 'quantity': 40}
            ]
        self.assertListEqual(self.coffee_service.get_invetory_status(), expected_inventory_status)
        self.coffee_service.reset_service()
    
    def test_3_outlets_success(self):
        input_json_file = open("input_json_2.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert(len(results.info) == 3)
        assert(len(results.warnings) == 1)
        assert(len(results.errors) == 0)
        assert(self.coffee_service.get_num_orders() == 3)
        assert(self.coffee_service.get_num_outlets() == 3)
        assert(len(self.coffee_service.low_quantity_indicator()) == 3)
        expected_inventory_status = [
            {'name': 'hot_water', 'quantity': 0},
            {'name': 'hot_milk', 'quantity': 400},
            {'name': 'ginger_syrup', 'quantity': 60},
            {'name': 'sugar_syrup', 'quantity': 40},
            {'name': 'tea_leaves_syrup', 'quantity': 40}
            ]
        self.assertListEqual(self.coffee_service.get_invetory_status(), expected_inventory_status)
        self.coffee_service.reset_service()
    
    def test_no_ingredients_provided(self):
        input_json_file = open("input_json_3.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_input_data(input_json)
        results = self.coffee_service.process_order()

        assert(len(results.info) == 3)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(len(input_validation_results.errors) == 2)
        assert(self.coffee_service.get_num_orders() == 3)
        assert(self.coffee_service.get_num_outlets() == 3)
        assert(len(self.coffee_service.low_quantity_indicator()) == 0)
        expected_inventory_status = []
        self.assertListEqual(self.coffee_service.get_invetory_status(), expected_inventory_status)
        self.coffee_service.reset_service()
    
    def test_10_orders_with_10_outlets_success(self):
        input_json_file = open("input_json_4.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert(len(results.info) == 10)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(self.coffee_service.get_num_orders() == 10)
        assert(self.coffee_service.get_num_outlets() == 10)
        assert(len(self.coffee_service.low_quantity_indicator()) == 0)
        expected_inventory_status = [
            {'name': 'hot_water', 'quantity': 1500},
            {'name': 'hot_milk', 'quantity': 1500},
            {'name': 'ginger_syrup', 'quantity': 820},
            {'name': 'sugar_syrup', 'quantity': 720},
            {'name': 'tea_leaves_syrup', 'quantity': 760}
            ]
        self.assertListEqual(self.coffee_service.get_invetory_status(), expected_inventory_status)
        self.coffee_service.reset_service()
    
    def test_10_orders_with_4_outlets_success(self):
        input_json_file = open("input_json_5.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert(len(results.info) == 10)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(self.coffee_service.get_num_orders() == 10)
        assert(self.coffee_service.get_num_outlets() == 4)
        assert(len(self.coffee_service.low_quantity_indicator()) == 0)
        expected_inventory_status = [
            {'name': 'hot_water', 'quantity': 1500},
            {'name': 'hot_milk', 'quantity': 1500},
            {'name': 'ginger_syrup', 'quantity': 820},
            {'name': 'sugar_syrup', 'quantity': 720},
            {'name': 'tea_leaves_syrup', 'quantity': 760}
            ]
        self.assertListEqual(self.coffee_service.get_invetory_status(), expected_inventory_status)
        self.coffee_service.reset_service()
    
    def test_invalid_input(self):
        input_json_file = open("input_json_7.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_input_data(input_json)
        results = self.coffee_service.process_order()

        assert(len(results.info) == 0)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(len(input_validation_results.errors) == 3)
    
    def test_empty_json_input(self):
        input_json_file = open("input_json_6.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_input_data(input_json)
        results = self.coffee_service.process_order()

        assert(len(results.info) == 0)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(len(input_validation_results.errors) == 4)
    
    def test_string_quantity_input(self):
        input_json_file = open("input_json_8.json", 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_input_data(input_json)
        results = self.coffee_service.process_order()

        assert(len(results.info) == 4)
        assert(len(results.warnings) == 0)
        assert(len(results.errors) == 0)
        assert(len(input_validation_results.errors) == 1)

if __name__ == '__main__':
    #pdb.set_trace()
    unittest.main()
import json
import pdb
import unittest

from services.CoffeeMachineService import CoffeeMachineService


class TestCoffeeMachine(unittest.TestCase):

    """
        Test suite to test all functionalities of
        Coffee Machine.
    """

    def setUp(self):
        self.coffee_service = CoffeeMachineService()
        self.test_files_folder = "test_inputs/"

    def tearDown(self):
        pass

    def test_4_outlets_success(self):
        """
            Check placing an order with 4 outlets machine.
            Input json has num outlets, ingredients info, 
            orders info.
        """
        input_json_file = open(
            f"{self.test_files_folder}/4_outlet_order_valid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert len(results.info) == 4
        assert len(results.warnings) == 1
        assert len(results.errors) == 0
        assert self.coffee_service.get_num_orders() == 4
        assert self.coffee_service.get_num_outlets() == 4
        assert len(self.coffee_service.low_quantity_indicator()) == 3
        expected_inventory_status = [
            {"name": "hot_water", "quantity": 200},
            {"name": "hot_milk", "quantity": 0},
            {"name": "ginger_syrup", "quantity": 60},
            {"name": "sugar_syrup", "quantity": 40},
            {"name": "tea_leaves_syrup", "quantity": 40},
        ]
        self.assertListEqual(
            self.coffee_service.get_invetory_status(), expected_inventory_status
        )
        self.coffee_service.reset_service()

    def test_3_outlets_success(self):

        """
            Check placing an order with 3 outlets machine.
            Input json has num outlets, ingredients info, 
            orders info.
        """

        input_json_file = open(
            f"{self.test_files_folder}/3_outlet_order_valid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert len(results.info) == 3
        assert len(results.warnings) == 1
        assert len(results.errors) == 0
        assert self.coffee_service.get_num_orders() == 3
        assert self.coffee_service.get_num_outlets() == 3
        assert len(self.coffee_service.low_quantity_indicator()) == 3
        expected_inventory_status = [
            {"name": "hot_water", "quantity": 0},
            {"name": "hot_milk", "quantity": 400},
            {"name": "ginger_syrup", "quantity": 60},
            {"name": "sugar_syrup", "quantity": 40},
            {"name": "tea_leaves_syrup", "quantity": 40},
        ]
        self.assertListEqual(
            self.coffee_service.get_invetory_status(), expected_inventory_status
        )
        self.coffee_service.reset_service()

    def test_no_ingredients_provided(self):
        """
            Check placing an order with no ingredients info.
            Input json has num outlets, orders info.
        """
        input_json_file = open(
            f"{self.test_files_folder}/ingredients_missing_invalid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_full_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 3
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 2
        assert self.coffee_service.get_num_orders() == 3
        assert self.coffee_service.get_num_outlets() == 3
        assert len(self.coffee_service.low_quantity_indicator()) == 0
        expected_inventory_status = []
        self.assertListEqual(
            self.coffee_service.get_invetory_status(), expected_inventory_status
        )
        self.coffee_service.reset_service()

    def test_10_orders_with_10_outlets_success(self):
        """
            Check placing an 10 orders with 10 outlets machine.
            Input json has num outlets, ingredients info, 
            orders info.
        """
        input_json_file = open(
            f"{self.test_files_folder}/10_orders_10_outlets_valid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert len(results.info) == 10
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert self.coffee_service.get_num_orders() == 10
        assert self.coffee_service.get_num_outlets() == 10
        assert len(self.coffee_service.low_quantity_indicator()) == 0
        expected_inventory_status = [
            {"name": "hot_water", "quantity": 1500},
            {"name": "hot_milk", "quantity": 1500},
            {"name": "ginger_syrup", "quantity": 820},
            {"name": "sugar_syrup", "quantity": 720},
            {"name": "tea_leaves_syrup", "quantity": 760},
        ]
        self.assertListEqual(
            self.coffee_service.get_invetory_status(), expected_inventory_status
        )
        self.coffee_service.reset_service()

    def test_10_orders_with_4_outlets_success(self):

        """
            Check placing an 10 orders with 4 outlets machine.
            Input json has num outlets, ingredients info, 
            orders info.

            Machine will serve 4 orders parallely at once.
            Next 4 in next turn.
        """

        input_json_file = open(
            f"{self.test_files_folder}/10_orders_4_outlets_valid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        results = self.coffee_service.process_order()

        assert len(results.info) == 10
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert self.coffee_service.get_num_orders() == 10
        assert self.coffee_service.get_num_outlets() == 4
        assert len(self.coffee_service.low_quantity_indicator()) == 0
        expected_inventory_status = [
            {"name": "hot_water", "quantity": 1500},
            {"name": "hot_milk", "quantity": 1500},
            {"name": "ginger_syrup", "quantity": 820},
            {"name": "sugar_syrup", "quantity": 720},
            {"name": "tea_leaves_syrup", "quantity": 760},
        ]
        self.assertListEqual(
            self.coffee_service.get_invetory_status(), expected_inventory_status
        )
        self.coffee_service.reset_service()

    def test_invalid_input(self):
        """
            test invalid input where ingredients, orders/beverage info is
            missing while placing order.
        """
        input_json_file = open(
            f"{self.test_files_folder}/ingredients_beverages_missing_invalid_json.json",
            "r",
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_full_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 3

    def test_empty_json_input(self):

        """
            test invalid input where ingredients, orders/beverage, outlets
            info is missing while placing order.

            All required info are missing.
        """

        input_json_file = open(f"{self.test_files_folder}/empty_json.json", "r")
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_full_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 4

    def test_string_quantity_input(self):

        """
            test invalid input where ingredients, orders/beverage quantity value
            is in string not integer. Currently machine only accepts integer
            quantity values.
        """

        input_json_file = open(
            f"{self.test_files_folder}/quantity_as_string_invalid_input.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_full_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 4
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 1

    def test_valid_ingredients_input(self):

        """
            Test valid ingredients input json.
            Checking validate_ingredients_input_data method.
        """

        input_json_file = open(
            f"{self.test_files_folder}/total_items_quantity.json", "r"
        )
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_ingredients_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 0

    def test_valid_beverages_input(self):

        """
            Test valid beverages input json.
            Checking validate_beverages_input_data method.
        """

        input_json_file = open(f"{self.test_files_folder}/beverages.json", "r")
        input_json: dict = json.load(input_json_file)
        input_json_file.close()
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_beverages_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 0

    def test_invalid_ingredients_input(self):

        """
            Test invalid ingredients input json.
            Checking validate_ingredients_input_data method.
        """

        input_json: dict = {}
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_ingredients_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 1

    def test_invalid_beverages_input(self):

        """
            Test invalid beverages input json.
            Checking validate_beverages_input_data method.
        """

        input_json: dict = {}
        self.coffee_service.reset_service()
        self.coffee_service.set_machine_data(input_json)
        self.coffee_service.add_ingredients_to_inventory()
        self.coffee_service.reset_results()
        input_validation_results = self.coffee_service.validate_beverages_input_data(
            input_json
        )
        results = self.coffee_service.process_order()

        assert len(results.info) == 0
        assert len(results.warnings) == 0
        assert len(results.errors) == 0
        assert len(input_validation_results.errors) == 1


if __name__ == "__main__":

    unittest.main()

import json

from jsonschema import validate


class ValidateInputService:
    '''
         class used for validating vending
         machine inputs.
         Can be extended to validate other 
         types of inputs for any kind of
         vending machine.
    '''

    _coffee_machine_full_input_schema = {
        "type": "object",
        "properties": {
            "machine": {
                "type": "object",
                "properties": {
                    "outlets": {
                        "type": "object",
                        "properties": {"count_n": {"type": "integer"}},
                        "required": ["count_n"],
                    },
                    "total_items_quantity": {"type": "object"},
                    "beverages": {"type": "object"},
                },
                "required": ["outlets", "total_items_quantity", "beverages"],
            }
        },
        "required": ["machine"],
    }

    _coffee_machine_ingredients_input = {
        "type": "object",
        "properties": {"total_items_quantity": {}},
        "required": ["total_items_quantity"],
    }

    _coffee_machine_beverages_input = {
        "type": "object",
        "properties": {"beverages": {}},
        "required": ["beverages"],
    }

    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_coffee_machine_full_input(user_input_json):
        validate(
            instance=user_input_json,
            schema=ValidateInputService._coffee_machine_full_input_schema,
        )

    @staticmethod
    def validate_coffee_machine_ingredients_input(user_input_json):
        validate(
            instance=user_input_json,
            schema=ValidateInputService._coffee_machine_ingredients_input,
        )

    @staticmethod
    def validate_coffee_machine_beverages_input(user_input_json):
        validate(
            instance=user_input_json,
            schema=ValidateInputService._coffee_machine_beverages_input,
        )

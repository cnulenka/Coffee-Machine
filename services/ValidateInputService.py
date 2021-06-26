import json
from jsonschema import validate

class ValidateInputService:

    _coffee_machine_input_schema_1 = {
            "type":"object",
            "properties":{
                "machine":{
                    "type":"object",
                    "properties":{
                        "outlets":{
                        "type":"object",
                        "properties":{
                            "count_n":{
                                "type":"integer"
                            }
                        },
                        "required":[
                            "count_n"
                        ]
                        },
                        "total_items_quantity":{
                        "type":"object"
                        },
                        "beverages":{
                        "type":"object"
                        }
                    },
                    "required":[
                        "outlets",
                        "total_items_quantity",
                        "beverages"
                    ]
                }
            },
            "required":[
                "machine"
            ]
        }

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def validate_coffee_machine_input( user_input_json):
        validate(instance=user_input_json, schema= ValidateInputService._coffee_machine_input_schema_1)

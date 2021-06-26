from services.CoffeeMachineService import CoffeeMachineService
from utils.CoffeeMachineApp import CoffeeMachineApp
import json

def run():
    print("\n===================================================================")
    print("Please choose one of below options:")
    print("1. Run machine interactively")
    print("2. Run with Json input")
    print("Enter the choice number")
    print("===================================================================\n")
    choice = input()
    if choice == '1':
        print("\nPlease enter the number of outlets\n")
        num_outlets = input()
        coffee_machine = CoffeeMachineApp(num_outlets)
        coffee_machine.execute()
    elif choice == '2':
        print("\nPlease pass the input json file with num outlets, inventory, orders info\n")
        input_file_name = input()
        input_json_file = open(input_file_name, 'r')
        input_json: dict  = json.load(input_json_file)
        input_json_file.close()
        coffee_service = CoffeeMachineService(input_json=input_json)
        results = coffee_service.process_order()
        results.print_results()
        coffee_service.reset_service()
    else:
        print("Wrong Input!! Try again")

if __name__ == '__main__':
    run()
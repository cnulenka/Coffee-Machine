from services.CoffeeMachineService import CoffeeMachineService
from services.CoffeeMachineApp import CoffeeMachineApp
import json

def run():
    print("Please choose one of below options:")
    print("1. Run machine interactively")
    print("2. Run with Json input")
    print("Enter the choice number")
    choice = input()
    if choice == '1':
        print("Please enter the number of outlets")
        num_outlets = input()
        coffee_machine = CoffeeMachineApp(num_outlets)
        coffee_machine.execute()
    elif choice == '2':
        print("Please pass the input json file with num outlets, inventory, orders info")
        input_file_name = input()
        input_json_file = open(input_file_name, 'r')
        input_json = json.load(input_json_file)    
        input_json_file.close()
        coffee_service = CoffeeMachineService(input_json)
        coffee_service.process_order()
        coffee_service.reset()
    else:
        print("Wrong Input!! Try again")

if __name__ == '__main__':
    run()
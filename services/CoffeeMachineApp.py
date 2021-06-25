from operations.CoffeeMachineService import CoffeeMachineService
import json

'''
    class used to run coffee machine functionality
    interactively from the cmd
'''

class CoffeeMachineApp:

    def __init__(self, num_outlets) -> None:
        self._num_outlets = num_outlets
        self._coffee_service = CoffeeMachineService(num_outlets)
    
    def welcome_message(self):
        message = "Hi Welcome! \n" + \
            f"This Coffee machine has {self._num_outlets} outlets to serve your fav drinks.\n" + \
            "Enjoy your beverage :)\n"
        
        print("===================================================================")
        print(message)
        print("===================================================================")
    
    def show_options(self):
        message = "Please choose one of below options:\n" +\
            "1. Add/Update Inventory.\n" + \
            f"2. Order Beverage ({self._num_outlets} max at once)" +\
            "3. Reset Inventory" +\
            "4. exit\n" +\
            "Enter the choice number\n"
        
        print("===================================================================")
        print(message)
        print("===================================================================")

    def execute(self):
        self.welcome_message()
        self.show_options()
        while True:
            choice = input()
            if choice == "1":
                print("Please enter the json file name with Ingredients update info")
                ingredients_quantity_update_file_name = input()
                ingredients_quantity_update_file = open(ingredients_quantity_update_file_name, 'r')
                ingredients_quantity_update = json.load(ingredients_quantity_update_file)    
                ingredients_quantity_update_file.close()
                self._coffee_service.add_ingredients_to_inventory(ingredients_quantity_update)
                print("Inventory Updated!!")
            elif choice == "2":
                print("Please enter the json file name with desired beverage info")
                print(f" Only first {self._num_outlets} orders will be served!")
                print("Please provide the rest in next turn")
                beverages_order_file_name = input()
                beverages_order_file = open(beverages_order_file_name, 'r')
                beverages_order = json.load(beverages_order_file)    
                beverages_order_file.close()
                self._coffee_service.process_order(beverages_order)
                print("Order Served. Enjoy!! :)")
            elif choice == "3":
                self._coffee_service.reset()
                print("Inventory cleared.")
                print("Fill inventory before next order")
            elif choice == "4":
                print("Thank you! Have a nice day :)")
                break
            else:
                print("Wrong choice!!")
            self.show_options()
        

        '''
        Program Ends
        '''
        self._coffee_service.reset()
            
        
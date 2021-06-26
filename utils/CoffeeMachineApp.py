from services.CoffeeMachineService import CoffeeMachineService
import json

'''
    class used to run coffee machine functionality
    interactively from the cmd
'''

class CoffeeMachineApp:

    def __init__(self, num_outlets) -> None:
        self._coffee_service = CoffeeMachineService(num_outlets=num_outlets)
    
    def welcome_message(self):
        message = "Hi Welcome! \n" + \
            f"This Coffee machine has {self._coffee_service.get_num_outlets()} outlets to serve your fav drinks.\n" + \
            "Place Order and Enjoy your beverages :)"
        
        print("===================================================================")
        print(message)
        print("===================================================================\n")
    
    def show_options(self):
        message = "Please choose one of below options:\n" +\
            "1. Add/Update Inventory.\n" + \
            f"2. Order Beverages ({self._coffee_service.get_num_outlets()} max at once)\n" +\
            "3. Get Ingredients Quantity Status\n" +\
            "4. Reset Inventory\n" +\
            "5. Exit\n" +\
            "Enter the choice number"
        
        print("===================================================================")
        print(message)
        print("===================================================================\n")

    def execute(self):
        self.welcome_message()
        self.show_options()
        while True:
            choice = input()
            if choice == "1":
                print("\nPlease enter the json file name with Ingredients update info\n")
                ingredients_quantity_update_file_name = input()
                ingredients_quantity_update_file = open(ingredients_quantity_update_file_name, 'r')
                ingredients_quantity_update = json.load(ingredients_quantity_update_file)    
                ingredients_quantity_update_file.close()
                self._coffee_service.reset_results()
                self._coffee_service.add_ingredients_to_inventory(ingredients_quantity_update)
                results = self._coffee_service.low_quantity_indicator_message()
                print("\nInventory Updated!!\n")
                results.print_results()
            elif choice == "2":
                print("\nPlease enter the json file name with beverages order info")
                print(f"Only first {self._coffee_service.get_num_outlets()} orders will be served!")
                print("Please provide the rest in next turn\n")
                beverages_order_file_name = input()
                beverages_order_file = open(beverages_order_file_name, 'r')
                beverages_order = json.load(beverages_order_file)    
                beverages_order_file.close()
                self._coffee_service.reset_results()
                results = self._coffee_service.process_order(beverages_order)
                results.print_results()
                print("\nOrder Served. Enjoy!! :)\n")
            elif choice == "3":
                self._coffee_service.reset_results()
                status = self._coffee_service.get_invetory_status()
                if len(status) == 0:
                    print("\nInventory is empty!!\n")
                else:
                    print()
                    for ingredient in status:
                        name = ingredient["name"]
                        quantity = ingredient["quantity"]
                        print(f"Inventory has {quantity}ml of {name}")
                    print()
            elif choice == "4":
                self._coffee_service.reset_service()
                print("\nInventory cleared.")
                print("Fill inventory before next order\n")
            elif choice == "5":
                print("\nThank you! Have a nice day :)\n")
                break
            else:
                print("Wrong choice!!")
            self.show_options()
        

        '''
        Program Ends
        '''
        self._coffee_service.reset_service()
            
        
from operations.CoffeeMachine import CoffeeMachine
import sys
import json

def run(input_file_name):
    input_json_file = open(input_file_name, 'r')
    input_json = json.load(input_json_file)    
    input_json_file.close()
    coffee_machine = CoffeeMachine(input_json)
    coffee_machine.process()
    coffee_machine.reset()


if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 1:
        print("Please pass input json file as argument")
    else:
        input_file_name = sys.argv[1]
        run(input_file_name)
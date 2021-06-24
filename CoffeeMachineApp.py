from .models.CoffeeMachine import CoffeeMachine

def run(input_file_name: str):
    coffee_machine = CoffeeMachine.getInstance()
    coffee_machine.process()
    coffee_machine.reset()


if __name__ == '__main__':
    input_file_name = ""
    run(input_file_name)
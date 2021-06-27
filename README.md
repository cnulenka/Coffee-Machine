# Coffee-Machine

A multithreaded beverage order serving app. Uses threads and locks to serve N orders parallely. Shows warning to indicate ingredients running low in inventory.
See below for usage.<br>

### Usage

Execute the below command to run the program:

```bash
pip install -r requirements.txt
python main.py
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### There are 2 ways to interact with the application.

#### 1. Run machine interactively
    
![cmd_interactive_1](https://github.com/cnulenka/Coffee-Machine/blob/main/usage_screenshots/cmd_interactive_1.png)
    
![cmd_interactive_2](https://github.com/cnulenka/Coffee-Machine/blob/main/usage_screenshots/cmd_interactive_2.png)
    
![cmd_interactive_3](https://github.com/cnulenka/Coffee-Machine/blob/main/usage_screenshots/cmd_interactive_3.png)<br>

#### 2. Input a json file containing the inputs in the following format:

```
{
    "machine": {
      "outlets": {
        "count_n": 4
      },
      "total_items_quantity": {
        "hot_water": 500,
        "hot_milk": 500,
        "ginger_syrup": 100,
        "sugar_syrup": 100,
        "tea_leaves_syrup": 100
      },
      "beverages": {
        "hot_tea": {
          "hot_water": 200,
          "hot_milk": 100,
          "ginger_syrup": 10,
          "sugar_syrup": 10,
          "tea_leaves_syrup": 30
        },
        "hot_coffee": {
          "hot_water": 100,
          "ginger_syrup": 30,
          "hot_milk": 400,
          "sugar_syrup": 50,
          "tea_leaves_syrup": 30
        },
        "black_tea": {
          "hot_water": 300,
          "ginger_syrup": 30,
          "sugar_syrup": 50,
          "tea_leaves_syrup": 30
        },
        "green_tea": {
          "hot_water": 100,
          "ginger_syrup": 30,
          "sugar_syrup": 50,
          "green_mixture": 30
        }
      }
    }
  }
```
![run_with_input_json](https://github.com/cnulenka/Coffee-Machine/blob/main/usage_screenshots/run_with_input_json.png)

Whenever ingredients run low, a warning is displayed in the console.

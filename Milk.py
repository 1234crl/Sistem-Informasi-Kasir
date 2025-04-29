import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Milk.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingMilk():
    data = read()
    print("\nChoose Milk:")
    for key, value in data.items():
        print(f"{key}. {value}")

def inputMilk():
    while True:
        try:
            milk_input = int(input("Input the number of ordered milk: "))
            if 1 <= milk_input <= 3:
                return milk_input
            else:
                print("Milk is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getMilkByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]

def getMilkCostbyID(id):
    id = int(id)

    if id == 2 or id == 3:
        charge_milk = 5000
    else:
        charge_milk = 0
    return charge_milk


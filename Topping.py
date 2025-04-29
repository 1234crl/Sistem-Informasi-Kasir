import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Topping.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingTopping():
    data = read()
    print("\nChoose Topping:")
    for key,value in data.items():
        print(f"{key}. {value}")

def inputTopping():
    while True:
        try:
            topping_input = int(input("Input the number of topping you want: "))
            if 1 <= topping_input <= 5:
                return topping_input
            else:
                print("Topping is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getToppingByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]

def getToppingCostbyID(id):
    '''UNTUK INPUT DAN MENAMPILKAN TOPPING MINUMAN'''
    id = int(id)

    if 1< id <6:
        if id == 2:
            charge_topping = 4500
        elif id == 3:
            charge_topping = 5000
        elif id == 4:
            charge_topping = 4000
        elif id == 5:
            charge_topping = 8000
    else:
        charge_topping = 0
    return charge_topping

import json
import pathlib

filename=str(pathlib.Path(__file__).parent.resolve()) + "\\Coffee_Menu.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def write(data):
    with open(filename, 'w') as file:
        json.dump(data,file)

def OrderingCoffee():
    while True:
        try:
            order = int(input("Input the number of ordered menu: "))    
            if 1<=order<=8:
                return order
            else:
                print("Order is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getCoffeeMenubyID(id):
    id_str = str(id)
    data = read()
    if id_str in data:
        return data[id_str]
    else:
        return "Order is out of range. Please input again."

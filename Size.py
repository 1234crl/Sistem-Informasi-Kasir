import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Size.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingSize():
    data = read()
    print("\nChoosing Size:")
    for key, value in data.items():
        print(f"{key}. {value}")

def inputSize():
    while True:
        try:
            size_input = int(input("Input the number of ordered size: "))
            if 1 <= size_input <= 2:
                return size_input
            else:
                print("Size is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getSizeByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]

def getSizeCostbyID(id):
    id = int(id)

    if id == 2:
        charge_size = 4000
    else:
        charge_size = 0
    return charge_size

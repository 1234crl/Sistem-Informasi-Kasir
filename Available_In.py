import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Available_In.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingAvailable():
    data = read()
    print("\nAvailable In:")
    for key, value in data.items():
        print(f"{key}. {value}")

def inputAvailable():
    while True:
        try:
            available_input = int(input("Input the number of ordered drink (available in): "))
            if available_input == 1 or available_input == 2:
                return available_input
            else:
                print("Number is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getAvailableByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]

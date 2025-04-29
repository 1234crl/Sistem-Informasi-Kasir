import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Ice.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingIce():
    data = read()
    print("\nChoosing Ice Level:")
    for key, value in data.items():
        print(f"{key}. {value}")

def inputIce():
    while True:
        try:
            ice_input = int(input("Input the number of ordered ice level: "))
            if 1 <= ice_input <= 4:
                return ice_input
            else:
                print("Ice level is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getIceByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]
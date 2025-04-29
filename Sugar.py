import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Sugar.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def printingSugar():
    data = read()
    print("\nChoosing Sugar Level:")
    for key, value in data.items():
        print(f"{key}. {value}")

def inputSugar():
    while True:
        try:
            sugar_input = int(input("Input the number of ordered sugar level: "))
            if 1 <= sugar_input <= 6:
                return sugar_input
            else:
                print("Sugar level is out of range. Please input again.")
        except:
            print("Please input in number only.")

def getSugarByID(id):
    id_str = str(id)
    data = read()
    return data[id_str]
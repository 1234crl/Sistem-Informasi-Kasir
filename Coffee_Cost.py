import json 
import pathlib

filename=str(pathlib.Path(__file__).parent.resolve()) + "\\Coffee_Cost.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def write(data):
    with open(filename, 'w') as file:
        json.dump(data,file)

def getCoffeePricesByID(id):
    data = read()
    return data[id]


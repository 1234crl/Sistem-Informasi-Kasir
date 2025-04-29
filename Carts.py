import json 
import pathlib

filename=str(pathlib.Path(__file__).parent.resolve()) + "\\Carts.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def write(data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def add(numb):
    data = read()
    if str(numb["numb_order"]) not in data:
        data[numb["numb_order"]] = numb
        write(data)
        return True
    else:
        return False

def delete(numb):
    data = read()
    del data[numb]
    write(data)

#Masukin ke list
coffee_list = []
data = read()
for i in data.values():
    a = i["order"]
    coffee = {
        "coffee": a
    }
    print(coffee)
    coffee_list.append(coffee)

#Masukin ke DICT
print(coffee_list)
new_list = {
    "order": coffee_list
}

print(new_list)

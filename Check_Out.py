import json
import Carts
import pathlib

filename=str(pathlib.Path(__file__).parent.resolve()) + "\\Check_Out.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def write(data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def calculate(cash):
    data_carts = Carts.read()
    pay = True

    sum = 0
    for i in data_carts.values():
        coffee_price = i["prices"]
        sum+=coffee_price

    while pay == True:
        if cash >= sum:
            pay = False
            change = cash - sum
            return sum, change
        else:
            print("Sorry, your money balance isn't sufficient. Please input again.")
            cash = float(input("How much customer pay? \t"))

def add_to_struk():
    coffee_list = []
    data_carts = Carts.read()

    printing()
    for key in data_carts.keys():
        item = data_carts[key] 
        print(f"{item['amount']} {item['order']} {item['milk']} {item['available']} {item['size']} {item['topping']} {item['sugar']} {item['ice']} {item['prices']}")
    print(f"{'-'*70 :<70}")

    cash = float(input("How much customer pay? \t"))
    sum, change = calculate(cash)
    for i in data_carts.values():
        data_co = read()
        if data_co == {}:
            queue = 1
        else:
            queue = list(data_co.keys())[-1]
            queue = int(queue)
            queue+=1
        order_code = i["numb_order"]
        coffee_name = i["order"]
        coffee_amount = i["amount"]
        coffee_size = i["size"]
        coffee_price = i["prices"]

        coffee = {
            "order code" : order_code,
            "coffee" : coffee_name,
            "amount" : coffee_amount,
            "size"   : coffee_size,
            "prices" : coffee_price
        }
        coffee_list.append(coffee)
        
        new_list = {
        "queue": queue,
        "order": coffee_list,
        "total": sum,
        "cash" : cash,
        "change": change
                }
        Carts.delete(str(order_code))

    print(f"Total   : {sum :>60}")
    print(f"Cash    : {cash :>60}")
    print(f"Change  : {change :>60}")

    if queue not in data_co:
        data_co[new_list["queue"]] = new_list
        write(data_co)

def printing():
    data = read()
    queue = list(data.keys())[-1]

    print()
    print(f"{'Our Story Cafè' :^70}")
    print(f"{'-'*70 :<70}")
    print(f"{'Tunjungan Plaza 3' :^70}")
    print(f"{'Surabaya' :^70}")
    print(f"{'Queue No.' + (str(queue)) :^70}")
    print(f"{'OS: Cashier' :<70}")
    print(f"{'Cashier: YESA' :>70}")
    print(f"{'-'*70 :<70}")


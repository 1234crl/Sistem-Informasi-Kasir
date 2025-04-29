import os
import Coffee_Menu
import Coffee_Cost
import Milk
import Available_In
import Size
import Topping
import Sugar
import Ice
import Carts
import Check_Out

def header():
    '''To Print Out Header'''
    os.system("cls")
    print(f"{'*'*35 :^70}")
    print(f"{'Welcome to' :^70}")
    print(f"{'Our Story Cafè' :^70}")
    print(f"{'*'*70:^70}")
    print(f"{'A good day always starts with good coffee' :^70}")
    print(f"{'*'*70 :^70}")

def menu():
    print(f"{'|'} {'1. View Our Cafè Menu' :<67} {'|'}")
    print(f"{'|'} {'2. Removing Items From Carts' :<67} {'|'}")
    print(f"{'|'} {'3. View Carts':<67} {'|'}")
    print(f"{'|'} {'4. About Us':<67} {'|'}")
    print(f"{'|'} {'0. Quit Program':<67} {'|'}")
    print(f"{'-'*70 :^70}")

    while True:
        try:
            input_menu = int(input("Choose menu: "))
            if 0<=input_menu<=4:
                return input_menu
            else:
                print("Menu is out of range. Please input again.") 
        except:
            print("Please input in number only.")

def add():
    '''To Input + Add Items on a Dict'''
    data = Carts.read()
    if data == {}:
        numb = 110
    else:
        numb = list(data.keys())[-1]
    numb_int = int(numb) + 1

    order = Coffee_Menu.OrderingCoffee()    
    ordered_coffee = Coffee_Menu.getCoffeeMenubyID(order)
    prices = 0

    #CHOOSING TYPE OF MILK
    if order!=1 and order!=3:
        Milk.printingMilk()
        milk_input = Milk.inputMilk()
        prices = Milk.getMilkCostbyID(milk_input)
    else:
        milk_input = 0

    #AVAILABLE IN
    Available_In.printingAvailable()
    available_input = Available_In.inputAvailable()

    #CHOOSING SIZE
    Size.printingSize()
    size_input = Size.inputSize()
    Size.getSizeByID(size_input)
    prices += Size.getSizeCostbyID(size_input)

    #CHOOSING TOPPING
    if order > 1:
        Topping.printingTopping()
        topping_input = Topping.inputTopping()
        prices+=Topping.getToppingCostbyID(str(topping_input))
    else:
        topping_input = 1

    #CHOOSING SUGAR
    Sugar.printingSugar()
    sugar_input = Sugar.inputSugar()

    #CHOOSING ICE (FOR COLD BEVERAGE ONLY)
    if available_input == 2:
        Ice.printingIce()
        ice_input = Ice.inputIce()
    else:
        ice_input = 1

    jumlah = int(input("How many cups: "))
    cost = Coffee_Cost.getCoffeePricesByID(str(order))*jumlah
    prices += cost

    item = {
        "numb_order" : str(numb_int),
        "order" : ordered_coffee,
        "amount" : jumlah,
        "milk"  : Milk.getMilkByID(milk_input),
        "available" : Available_In.getAvailableByID(available_input),
        "size"  : Size.getSizeByID(size_input),
        "topping" : Topping.getToppingByID(topping_input),
        "sugar" : Sugar.getSugarByID(sugar_input),
        "ice": Ice.getIceByID(ice_input),
        "prices" : prices,
    }

    if Carts.add(item) == True:
        print("Item has been added.")

def menu_kopi():
    '''To Print Out The Menu'''
    print(f"{'MENU:' :^70}")
    print(f"{'*'*70 :^70}")

    data_coffee = Coffee_Menu.read()
    data_cost = Coffee_Cost.read()
    for i in data_coffee and data_cost:
        print(f"{'|'} {(i)+'. '+(data_coffee[i]) + ' '*(58-len(data_coffee[i])) + str((data_cost[i]))} {'|'}")
    print(f"{'-'*70 :^70}")
    add()

def viewcarts(option):
    '''TO VIEW CARTS BEFORE CHECK OUT'''
    data = Carts.read()
    if option == 2 or option == 3:
        print(f"{'YOUR PERSONAL CARTS' :^70}")
        for item in data.values():
            print(f"{item['numb_order']} {item['amount']} {item['milk']} {item['available']} {item['order']} {item['size']} {item['topping']} {item['sugar']} {item['ice']} {item['prices']}")
        print(f"{'-'*70 :<70}")

        if data == {}:
            print("You have not ordered anything.\n")    

        if option == 3 and data!={}:
            ask = True
            while ask == True:
                check_out = input("Are you ready to check out? (y/n): ")
                co_lower = check_out.lower()
                if co_lower == "y" or co_lower == "n":
                    if co_lower == "y":
                        Check_Out.add_to_struk()
                    ask = False
                else:
                    print("Please choose between yes or no (y/n) only.")

def more(): 
    '''TO ADD MORE ORDER'''
    input_more = True
    while input_more == True:  
        lagi = input("Do you want to get anything else? (y/n): ")
        lagi_lower = lagi.lower()
        if lagi_lower == "y":
            header(), menu_kopi()
        elif lagi_lower == "n":
            input_more = False
        else:
            print("Choose between yes or no (y/n) only.")

def cancel():
    '''TO REMOVE ITEMS FROM CARTS'''
    data = Carts.read()
    if data == {}:
        print("You have not ordered anything.\n")
    else:
        viewcarts(2)
        items_cancel = int(input("Input the code of item you want to remove: "))
        Carts.delete(str(items_cancel))
        print(f"Item has been deleted.")

def aboutus():
    os.system("cls")
    print(f"{'*'*35 :^70}")
    print(f"{'Our Story Cafè' :^70}")
    print()
    print(f"{'A cup of coffee for each of your story' :^70}")
    print(f"{'*'*70:^70}")
    print(f"{'1 Brand    20+ Outlets    8 Menu' :^70}")
    print(f"{'We honor simplicity and quality.' :^70}")
    print()
    print(f"{'You have a complaint or message for us?' :^70}")
    print(f"{'Immediately contact us and we are more than ready to help you' :^70}")
    print(f"{'Email: ourstorycafe@gmail.com         WA:0812763927291'  :^70}")
    print(f"{'*'*70 :^70}")


ordering = True
while ordering == True:
    header()
    opsi = menu()
    if opsi == 1:
        header(), menu_kopi(), more()
    elif opsi == 2:
        header(), cancel()
    elif opsi == 3:
        header(),viewcarts(opsi)
    elif opsi == 4:
        aboutus()
    elif opsi == 0:
        ordering = False
        print("Thank you. Have a nice day!^^")    
    os.system("pause")
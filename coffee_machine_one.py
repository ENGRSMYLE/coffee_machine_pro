
resources_available = {
    "Water": 300,
    "Coffee": 60,
    "Milk": 400,
    "Money": 0
}

flavours = {
    "expresso": {
        "water_amount": 50,
        "coffee_amount": 18,
        "milk_amount": 0,
        "cost": 2500
    },
    "latte": {
        "water_amount": 200,
        "coffee_amount": 24,
        "milk_amount": 150,
        "cost": 3000
    },
    "cappuccino": {
        "water_amount": 250,
        "coffee_amount": 24,
        "milk_amount": 100,
        "cost": 4500
    }
}


def add_milk(amount_of_milk):
    amount_of_milk = int(amount_of_milk)
    if amount_of_milk == 300:
        print("It will cost you $500 to add coffee")
        resources_available["Money"] -= 500
        resources_available["Milk"] += amount_of_milk
    elif amount_of_milk == 500:
        print("It will cost you $700 to add water")
        resources_available["Money"] -= 700
        resources_available["Milk"] += amount_of_milk
    else:
        resources_available["Milk"] += 0
    return resources_available["Milk"]


def add_coffee(amount_of_coffee):
    amount_of_coffee = int(amount_of_coffee)
    if amount_of_coffee == 300:
        print("It will cost you $500 to add coffee")
        resources_available["Money"] -= 500
        resources_available["Coffee"] += amount_of_coffee
    elif amount_of_coffee == 500:
        print("It will cost you $700 to add water")
        resources_available["Money"] -= 700
        resources_available["Coffee"] += amount_of_coffee
    else:
        resources_available["Coffee"] += 0
    return resources_available["Coffee"]


def add_water(amount_of_water):
    amount_of_water = int(amount_of_water)
    if amount_of_water == 300:
        print("It will cost you $500 to add water")
        resources_available["Money"] -= 500
        resources_available["Water"] += amount_of_water
    elif amount_of_water == 500:
        print("It will cost you $700 to add water")
        resources_available["Money"] -= 700
        resources_available["Water"] += amount_of_water
    else:
        resources_available["Water"] += 0
    return resources_available["Water"]


def enter():
    while True:
        order = input("What flavour of coffee do you want"
                      " (Type |'A' for 'expresso |'B' for 'latte' | 'C' for cappuccino)\n").upper()

        user_cash = int(input("Enter the amount that you have\n"))

        A = "expresso"
        B = "latte"
        C = "cappuccino"

        if order == "A":
            user_choice = flavours[A]
        elif order == "B":
            user_choice = flavours[B]
        elif order == "C":
            user_choice = flavours[C]

        if user_cash < user_choice["cost"]:
            print(f"Money is not enough to purchase ITEM")
            break
        if resources_available["Water"] < user_choice["water_amount"]:
            print("Water is not available")
            break
        if resources_available["Coffee"] < user_choice["coffee_amount"]:
            print("Coffee is not available")
            break
        if resources_available["Milk"] < user_choice["milk_amount"]:
            print("Milk is not available")
            break

        resources_available["Water"] -= user_choice["water_amount"]
        resources_available["Coffee"] -= user_choice["coffee_amount"]
        resources_available["Milk"] -= user_choice["milk_amount"]
        resources_available["Money"] += user_choice["cost"]

        # print(resources_available)

        print("Enjoy your coffee.......")
        if user_cash > user_choice["cost"]:
            user_change = user_cash - user_choice["cost"]
            print(f"Your change remaining is {user_change}")

        more_coffee = input("Do you want to purchase another coffee\n").lower()
        if more_coffee == "no":
            break

    password = "stephen"
    manager_control = input("Are you the manager of this coffee shop\n")
    if manager_control == "yes":
        ask_password = input("Enter the secret word to have access to manager control\n")
        if ask_password == password:
            print("Welcome to the  manager control option")
            what_to_do = input("What do you want to do"
                               " (Type 'A' to addMilk|| 'B' to addCoffee || 'C' to addWater )\n").upper()
            if what_to_do == "A":
                print("You can either add 300ml or 500ml of milk")
                milk_to_add = input("Enter the amount of milk you want to add\n")
                add_milk(milk_to_add)
                enter()
            elif what_to_do == "B":
                print("You can either add 300ml or 500ml of coffee")
                coffee_to_add = input("Enter the amount of coffee you want to add\n")
                add_coffee(coffee_to_add)
                enter()
            elif what_to_do == "C":
                print("You can either add 300ml or 500ml of water")
                water_to_add = input("Enter the amount of water you want to add\n")
                add_water(water_to_add)
                enter()
        else:
            print(f"You type the incorrect password")


use_coffee_machine = input("Do you want to use the coffee machine\n")
if use_coffee_machine == 'yes':
    enter()














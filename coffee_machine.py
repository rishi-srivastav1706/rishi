MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]> resources[item]:
            print(f"sorry {item} not sufficient")
            return False
    return True

def process_coin():
    print("please insert coin.")
    total = int(input("how many quarter: "))*0.25
    total+= int(input("how many demies: "))*0.10
    total += int(input("how many pennes:"))*0.01
    total += int(input("how many nickels: "))*0.05
    return total
def transaction_is_successful(money_received, drink_cost):
    if money_received>drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"here is {change} change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry the money is not enough")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on =True
while is_on:
    choice = input("what would you like to order (espresso, latte, capuccino): ")
    if choice == "off":
        is_on =False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_is_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


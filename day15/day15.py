import sys
from datacof import resources,money,MENU

def ask():
    ask1 = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    return ask1

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a number greater than or equal to 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def report():
    for entry in resources:
        print(f"{entry.capitalize()}: {resources[entry]}")
    print(f"Money: ${money}")

def insert_coins(tipo):
        global money
        price = tipo['cost']
        print(f"Price: {price}")
        total = get_positive_integer("How many quarters ($0.25): ")*0.25
        total += get_positive_integer("How many dimes ($0.10): ")*0.1
        total += get_positive_integer("How many nickles ($0.05): ")*0.05
        total += get_positive_integer("How many pennies ($0.01): ")*0.01
        if total < price:
            print('Insufficient money! Money refunded\n')
            return False
        elif total > price:
            change = total - price
            print(f"Here is ${round(change,1)} in change\n")
            money += price
            return True
        else: 
            money += price
            return True

def check(ingredients):
    possible = True
    for ing in ingredients:
        if resources[ing] < ingredients[ing]:
            print(f"Sorry there is no enough {ing}.")
            possible = False
    return possible

def coffee(user):
    ingredients = MENU[user]["ingredients"]
    if check(ingredients):
        if insert_coins(MENU[user]):
            for ing in ingredients:
                resources[ing] -= ingredients[ing]
            print(f"Here is your {user}. Enjoy!")

def recharge():
    for ing in resources:
        resources[ing] += get_positive_integer(f"How much {ing} was added? ")
    

while True:
    user = ask()
    if user == 'off':
        sys.exit()
    elif user == 'report':
        report()
    elif user == 'recharge':
        recharge()
    elif user in ['latte','cappuccino','espresso']:
        coffee(user)
    else:
        print("Option not available")



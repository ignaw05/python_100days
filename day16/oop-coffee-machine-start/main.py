from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    ask1 = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()
    if ask1 == 'report':
        coffee_maker.report()
        money_machine.report()
    elif ask1 == 'off':
        sys.exit()
    elif ask1 in ['latte','cappuccino','espresso']:
        order = menu.find_drink(ask1)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    else: print("Option unavailable!")

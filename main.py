from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()

    drink = None
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            print(f"That would be {drink.cost}$")
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)

print("Shutting down...")
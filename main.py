from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

choice = "on"
while choice != "off":
    drink = None
    while drink is None:
        choice = input(f"What would you like? {menu.get_items()}: ").lower()
        if choice == "off":
            print("shutting down...")
            exit()
        elif choice == "report":
            coffeemaker.report()
            moneymachine.report()
        else:
            drink = menu.find_drink(choice)

    if coffeemaker.is_resource_sufficient(drink):
        print(f"That would be {drink.cost}$")
        if moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)

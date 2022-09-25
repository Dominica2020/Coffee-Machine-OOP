from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 4: Check if resources are sufficient (& that item is in menu)
# TODO 5: Process coins if resources are sufficient
# TODO 6: Check if transaction if successful: too little? too much? Add to profit
# TODO 7: Make coffee: subtract resources then hand over drink to user!


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

in_service = True
while in_service:
    request = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if request == "off":
        in_service = False
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if not drink:
            continue
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

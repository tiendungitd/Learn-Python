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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_off = False
spend: int = 0


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    print(ingredients)
    for key in ingredients:
        if ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def check_transaction(drink, total_coins):
    drink_cost = MENU[drink]["cost"]
    global spend
    if total_coins >= drink_cost:
        change_money = round(total_coins-drink_cost, 2)
        if change_money > 0:
            print(f"Here is {change_money} dollars in change")
        spend += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def resources_deduction(drink):
    ingredients = MENU[drink]["ingredients"]
    #global resources
    for key in ingredients:
        resources[key] -= ingredients[key]


while not turn_off:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        turn_off = True
    elif user_input == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        if spend > 0:
            print(f"Money: ${spend}")
    elif user_input in ["espresso", "latte", "cappuccino"] and check_resources(user_input):
        print("Please insert coins")
        quarters_input = int(input("How many quarters?: "))
        dimes_input = int(input("How many dimes?: "))
        nickles_input = int(input("How many nickles?: "))
        pennies_input = int(input("How many pennies?: "))
        total_coins = 0.25*quarters_input + 0.1*dimes_input + 0.05*nickles_input + 0.01*pennies_input
        if check_transaction(user_input, total_coins):
            resources_deduction(user_input)
            print(f"Here is your {user_input}.☕ Enjoy!")





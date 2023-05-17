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

income = 0


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    if "milk" not in ingredients:
        ingredients["milk"] = 0
    for key, value in resources.items():
        if resources[key] < ingredients[key]:
            resources[key] = resources[key] - 0
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coins(drink):
    global income
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    cost = MENU[drink]["cost"]

    print("Please insert coins.")
    quarter_count = int(input("how many quarters?"))
    dime_count = int(input("how many dimes?"))
    nickle_count = int(input("how many nickles?"))
    penny_count = int(input("how many pennies?"))

    payment = round(quarter_count * quarters + dime_count * dimes + nickle_count * nickles + penny_count * pennies, 2)
    if payment >= cost:
        change = payment - cost
        print(f"here is ${change} in change.")
        income += cost
    else:

        print("Sorry that's not enough money. Money refunded.")
        income + 0
        return False
    return True


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for key, value in resources.items():
        if resources[key] >= ingredients[key]:
            resources[key] = resources[key] - ingredients[key]
    print(f"here is your {drink} ☕.Enjoy!")



def choose_drink():
    global resources
    global income

    chosen_drink = input("What would you like? (espresso/latte/cappuccino)").lower()
    drinks = MENU.keys()
    if chosen_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${income}")
    else:
        for drink in drinks:
            if chosen_drink == drink:
                resources_sufficient = check_resources(chosen_drink)
                if resources_sufficient:
                    payment = process_coins(drink)
                    if payment is True:
                        make_coffee(drink)

    return chosen_drink


def main():
    machine_on = True
    while machine_on:
        drink = choose_drink()
        if drink == "off":
            machine_on = False


if __name__ == "__main__":
    main()

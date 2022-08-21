from pyparsing import re


def get_ingredient(user,MENU):
    """Take user choice and return sufficient amout of ingredient"""

    user_choice = MENU[user]
    ingredient_dict = user_choice["ingredients"]
    water_amount = ingredient_dict["water"]
    coffee_amount = ingredient_dict["coffee"]
    if user in ["latte","cappuccino"]: 
        milk_amount = ingredient_dict["milk"]
    else:
        milk_amount = 0
    cost_value = user_choice["cost"]
    return water_amount,coffee_amount,milk_amount,cost_value

def make_coffee(user):
    
    if user == "espresso":
        check_resources(user)
        process_coin(user)
  
    elif user in ["latte","cappuccino"]:
        check_resources(user)
        process_coin(user)

    else:
        print("you have choose wrong choice")
   
def check_resources(user_input):
    water_amount,coffee_amount,milk_amount,_ = get_ingredient(user_input,MENU)
    if water_amount <= resources["water"] and milk_amount <= resources["milk"] and coffee_amount <= resources["coffee"]:
        resources["water"] -= water_amount
        resources["milk"] -= milk_amount
        resources["coffee"] -= coffee_amount
        print(f" there is sufficient amount of {resources['water']}ml water and {resources['coffee']}g")

    else:
        print(f"there is insufficient amount of {resources['water']}ml water and {resources['coffee']}g left")


def process_coin(user):
    print("please insert the coin")
    user_quart = int(input("how many quarters?"))
    user_dimes = int(input("how many dimes?"))
    user_nickles = int(input("how many nickles?"))
    user_pennies = int(input("how many pennies?"))
    calculate = 0.25 * user_quart + 0.10 * user_dimes + 0.05 * user_nickles + 0.01 * user_pennies
    _,_,_,cost_value = get_ingredient(user,MENU)
    if calculate >= cost_value:
        report_dict["profit"] += cost_value
        if calculate > cost_value:
            change = calculate - cost_value
            print(f"here is your change {change}")
        print(f"enjoy your {user} coffee!")   


    else:
        print("Sorry that's not enough money. ")





if __name__ == "__main__":
    from main import MENU,resources
    report_dict = {"water":resources['water'],"milk":resources['milk'],"coffee" :resources['coffee'], "profit":0.0}
    off = False
    while not off: 
        user = input("what would you like to have? espresso/latte/cappuccino:")
        if user == "off":
            break
        if user == "report":
            print(f" Water: {resources['water']}ml/n ,Milk: {resources['milk']}ml/n, Coffee :{resources['coffee']}g, profit:{report_dict['profit']}")
            user = input("what would you like to have? espresso/latte/cappuccino:")
            make_coffee(user)
        else:
            make_coffee(user)
# # Creating a nested dictionary for having menu.
# MENU = {
#     'cappuccino': {
#         'ingredients': {
#             'water': 300,
#             'coffee': 30,
#         },
#         'cost': 2.5,
#     },
#     'latte': {
#         'ingredients': {
#             'water': 250,
#             'coffee': 75,
#         },
#         'cost': 3.5,
#     },
#     'espresso': {
#         'ingredients': {
#             'water': 250,
#             'coffee': 75,
#         },
#         'cost': 4.5,
#     },
# }
#
# # Creating a dictionary for having resources
# resources = {
#     'water': 500,
#     'milk': 250,
#     'coffee': 100,
# }
# profit = 0
#
#
# # Making a function for checking if there is no enough resources.
# def tank(order):
#     is_enough = True
#     for item in order:
#         if order[item] > resources[item]:
#             print(f"Sorry,there is no enough {item}")
#             is_enough = False
#     return is_enough
#
#
# # Making a function for getting money from user.
# def get_money():
#     total = int(input("Please insert coins"))
#     return total
#
#
# # Making a function for checking if received money is more than the price.
# def calc(money, cost):
#     if money > cost:
#         change = round(money - cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# # Making a function for making users order.
# def make(drink_name, ingredients):
#     for item in ingredients:
#         resources[item] -= ingredients[item]
#     print(f"Here is your {drink_name}")
#
#
# # Making a while loop for continue getting order or turn off the machine.
# is_on = True
# while is_on:
#     ask_user = input("What would you like?(espresso,latte,cappuccino,report,OFF) : ").lower()
#     if ask_user == 'off':
#         print("The machine is gonna off")
#         is_on = False
#     elif ask_user == 'report':
#         print(f"We have {resources} in resources.")
#     else:
#         drink = MENU[ask_user]
#         if tank(drink["ingredients"]):
#             payment = get_money()
#             calc(payment, drink['cost'])
#             make(ask_user, drink['ingredients'])
# # END OF PROJECT

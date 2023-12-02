# Gold = "Gold coins"
# def defeat_monsters_in_dungeon():
#     dungeon = [
#         "Goblin", 
#         "Gold coins", 
#         "Dragon",
#         "Dragon",
#         "Bandit",
#         "Gold coins",
#         "Giant Snake"]    
#     for monster in range(len(dungeon)):
#         if dungeon[monster] != "Gold coins":
#             dungeon[monster] = "Gold coins"
#         else:
#             continue
#     print(dungeon)

# defeat_monsters_in_dungeon()


def update_warehouse_product_database():
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }
    
    # To compare two dictonaries 

    # first start a new dictonary to store difference 
    New_Stock_Value = {}

    # a for loop that uses key and value (for , in , {variable}.items())
    # check if the key is in second dictonary
    for key, value in warehouse_product_database.items():
        if key in todays_orders:
            # new dictonary = value 1st dictonary - 2nd dictonary
            New_Stock_Value[key] = value - todays_orders[key]

        else:
            # add new items to 1st dictonary
            New_Stock_Value[key] = value

    # Second for loop if the key is not in in warehouse  
    for key, value in todays_orders.items():
        if key not in warehouse_product_database:
            New_Stock_Value[key] = (0 - value)
    
    # Print the original dictionaries and the difference dictionary
    print("The original dictionary 1 : ", warehouse_product_database)
    print("The original dictionary 2 : ", todays_orders)
    print("The difference dictionary is : ", New_Stock_Value)

update_warehouse_product_database()
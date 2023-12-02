# colours = {
#     "brown": 232,
#     "green": 55,
#     "grey": 977,
#     "red": 2314335,
#     "blue": 242,
#     "yellow": 903
# }

# Used_in_painting = {
#     "brown": 132,
#     "green": 25,
#     "grey": 677,
#     "red": 1219979,
#     "blue": 212,
#     "yellow": 303
# }

# def find_colours_used():
#     Colour_Difference = {}
#     for key, value in colours.items():
#         if key in Used_in_painting:
#             Colour_Difference[key] = value - Used_in_painting[key]
#         else:
#             Colour_Difference[key] = value
    
#     for key, value in Used_in_painting.items():
#         if key not in colours:
#             Colour_Difference = (0 - value)
    
#     print(Colour_Difference)

# find_colours_used()



New_Cars = {
    0: "Ford",
    1: "Jeep",
    2: "Nissan",
    3: "Toyota",
    4: "Subaru"
}

Other_Cars = {
    0: "Ford",
    1: "Jeep",
    2: "Nissan",
    3: "Toyota",
    4: "Subaru",
    5: "Holden",
    6: "Fiat",
    7: "Tesla"
}

def update_cars():
    Difference = {}

    for key, value in New_Cars.items():
        if value in Other_Cars:
            Difference[value] = Other_Cars[value] + key
        else:
            Difference[value] = key

    for key, value in Other_Cars.items():
        if value != New_Cars:
            Difference[value] = key
        else:
            continue
    print(Difference)
update_cars()



























from pprint import pprint

'''
List of dictonaries where each dictonary - detail of each contact in phonebook

[
    {
    "name": "John Smith",
    "address": "brisbane",
    "Phone": {
        "home": "121212",
        "Mobile": "2223"
        }
    },
    {
        "name": "melbourne",
        "address": "melbourne",
        "Phone": {
            "home": "3908304",
            "Mobile": 2930238
        }
    }
]
'''

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "12312312",
            "mobile": "213124"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Melbourne",
        "phone": {
            "home": "4123412",
            "mobile": "21312"
        }
    }
]

name = input("Enter name: ")
address = input("Enter address: ")
home = input("Enter home: ")
mobile = input("Enter mobile: ")

# create a dictonary
contact_to_add = {
    "name": name,
    "address": address,
    "phone": {
        "Home": home,
        "Mobile": mobile
    }
}

for phone in phonebook:
    for home in phone:
        if home == number or mobile == number:
            print(f"Number found {number} = {[home]}")
            break
        else:
            continue
    
        


# append to list
phonebook.append(contact_to_add)

pprint(phonebook)
def Check_login():
    Username_input = input()
    Password_input = input("Please Enter Password \n")
    attempt = 0

    while attempt < 5:
        for key, value in user_name_logins.items():
            if key == Username_input:
                if Password_input == user_name_logins:
                    Print("Succesful Login")
                    break
                else:
                    print("Wrong password try again")
                    attempt += 1
                    break
            else:
                print("wrong Username try Again")
                attempt += 1
                break
        

user_name_logins = {
    "chris": "Hello",
    "Ryan": "Bat",
    "ben": "Smart"
}



Check_login()



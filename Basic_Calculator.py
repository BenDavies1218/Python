print("Hello Welcome to the Calculator App") 
First_number = float(input("Please enter first Number: "))
print("Please choose from the the following: ")

userinput = int(input("1 = Add \n2 = Subtract \n3 = Divide \n4 = Multiple\n"))

Second_number = float(input("Please enter Second Number: "))

if userinput == 1 :
    print(str(First_number), "+", str(Second_number), "=", First_number + Second_number)
    exit()
elif userinput == 2 :
    print(str(First_number), "-", str(Second_number), "=", First_number - Second_number)
    exit()
elif userinput == 3 :
    print(str(First_number), "/", str(Second_number), "=", First_number / Second_number)
    exit()
elif userinput == 4 :
    print(str(First_number), "x", str(Second_number), "=", First_number * Second_number)
    exit()
else :
    print("Invalid Input Please try again")
    exit()
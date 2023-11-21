print("Hello Welcome to the Calculator App") 
again = "y"
while again == "y" or again == "Y" or again == "YES" or again == "Yes" or again == "Yes" or again == "yes" :
    
    First_number = float(input("Please enter first Number: "))
    
    print("Please choose from the the following: ")
    userinput = int(input("1 = Add \n2 = Subtract \n3 = Divide \n4 = Multiple\n"))

    Second_number = float(input("Please enter Second Number: "))
    
    # Add
    if userinput == 1 :
        print("Answer =  ",str(First_number), "+", str(Second_number), "=", First_number + Second_number)
        again = str(input("Do another Calculation? Y / N: \n"))
    # Subract
    elif userinput == 2 :
        print("Answer =  ",str(First_number), "-", str(Second_number), "=", First_number - Second_number)
        again = str(input("Do another Calculation? Y / N: \n"))
    # Divide
    elif userinput == 3 :
        print("Answer =  ",str(First_number), "/", str(Second_number), "=", First_number / Second_number)
        again = str(input("Do another Calculation? Y / N: \n"))
    # Multiply
    elif userinput == 4 :
        print("Answer =  ",str(First_number), "x", str(Second_number), "=", First_number * Second_number)
        again = str(input("Do another Calculation? Y / N: \n"))
    # Invalid Entry
    else :
        print("Invalid Input Please try again")
        again = str(input("Do another Calculation? Y / N: \n"))
exit()
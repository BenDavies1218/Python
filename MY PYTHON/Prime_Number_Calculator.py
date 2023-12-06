again = "y"
while again in ["y", "Y", "Yes", "YES", "yes"]:
    low_value = int(input ("Please Enter the Lowest Value you want to calculate: "))  
    high_value = int(input ("Please Enter the Highest Value you want to calculate: "))  

    print ("The Prime Numbers in that range are: ")  
    for number in range (low_value, high_value + 1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                print(number)
    
    again = input("Do another Calculation? Y / N: \n")
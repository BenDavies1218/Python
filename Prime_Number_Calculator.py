lower_value = int(input ("Please, Enter the Lowest Value you want to calculate: "))  
upper_value = int(input ("Please, Enter the Highest Value you want to calculate: "))  

print ("The Prime Numbers in that range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number) 
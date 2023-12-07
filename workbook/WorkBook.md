## _Question 1_
- Tags
    - Tags are used in Markup languages such as HTML5 to create elements on a webpage, these elements can then be referenced and styled using CSS or SCSS. When Creating a Webpage Developers should use Semantic Tags, these give the computer and other developers more definition to what a particular element is. Most Semantic Tags also contain default styling, meaning a H1 Semantic tag will have a larger Font size than H4 Semantic Tag.  

- Element Attributes
  - Elements on a Webpage can contain attributes these attributes can be used to add refenerence, functionality, style and many other things. Attributes that are commonly used are class and IDs, these add referencing so when we style an element we can add styling to every element with that specific class or an individually style an element with a specific ID.  

- Nesting Elements
  - One Functionality of Super Cascading Style Sheets (SCSS) is its ability to nest elements when referencing them. The code below Utilizes Nested elements:
  ```
  body {
    header {
        color: Blue;
        button {}
        logo {}
    }
    main {}
    footer {}
  }
  ```
  I found this to be most helpful when developing my website as this allowed me quickly and easily style my webpage. It organises your code in a way that is easy to read and also has the benefit of making your code more DRY. (Meaning you don't have to repeat yourself)(Meaning you don't have to repeat yourself)

## _Question 2_
Packets
  - When data is sent between two or more computers it's almost aways broken down into smaller files called packets, a packet normally consists of a header and data. 
  The header contains information about the packets data, its origin and its final destination. The Data conatins Data / information. Breaking data into small packets allows it to be routed much faster, 
  packets may take different routes to the same IP, this in turn helps to minimise Network traffic.

IP adresses (IPv4 vs IPv6)
  - An IP address is assigned to any computer when it connects to the interent, the IP acts as identification for the computer this allows it to send and recieve data.
    - IPv4 is a 32 bit binary code and is the fourth verson the Internet Protocal (IP), there are around 4.3 billion IPv4 unique addresses. While this is a large number it's insuffiecent to meet the worlds growing demains for the interent. IPv6 is the supersede to IPv4, it has a around 320 undecillion unique addresses and aims to provide a unique IP to each device connected to the internet. It's a 128 bit binnary code and uses static routing which makes sending data more secure while using less bandwidth. IPv6 was developed in 1996 and is still yet to be widely used in society because to various network upgrades that need to take place.

Routers and Routing
  - A router is part of the network infastructure its core job it determine the best route that the data packets should take to reach there intended IP. Routing is the name Given to the path the information took to reach its intended destination. 

Domains and DNS
  - A Domain is an Address on the interent, domains allow us to assign a name to Servers (IP). Rather than using the IP of the server Directly, which will also work when attempting to receive information from a specific server. 
  - A DNS converts a Domain Name that we can search for or type into our browser to a server IP address. DNS while unnessecary when browsing the internet is incredibaly important as remembering a 32 byte or 128 binary code for every website we visit isn't very convenient.

## _Question 3_ 
 TCP
   - Transmission Control Protocol (TCP) is a set rules that governs how data it send between two IPs. it defines:
     - Initalizes Connection between the two IPs
     - Defines how Data is Packaged
     - How the data packets will be routed
     - The order the packets will be sent
 
 HTTP and HTTPS
- Hypertext Transfer Protocol (HTTP) is the governing rules that allow webpages to communicate with a server, when we interact with a webpage the HTTP makes a request to the server. when we make a HTTP request we can transfer data between the our IP and server or vice versa. some common requests are: 
     - GET
     - POST

- Hypertext Transfer Protocol Secure (HTTPS) is similar to HTTP as it is a Protocol or set of rules for transfering data between a user and a server, but HTTPS request encrypts the data before transfering it. HTTPS is much more secure and helps to protect sensitive data like passwords, personal information and ect.
- Web Browsers are applications that someone can use to view the data on the internet. There are many browsers available to users with Google Chrome and Safari being the most Common. One main features of a Web Browser is they have a URL or address bar where we can enter a server IP or domain name and the web Browser will look for that address. The Web Browser is also responsible for transfering data and code into a graphical interface for a user.

## _Question 4_
 Lists
   - A list in Python is a great way of assigning a variable a value when we have multiple pieces of data we want to store. Within a list we can store both simple data types and complex data types. We define a list by using square brackets [ ], for example view the code below that conatins Strings an integer and a dictonary:
```
ben_davies = [
    "Male", 27, "Full Stack Developer",
    {
        "favourite Language": "Python",
        "favourite code": "print("Hello World")"
    }
]
```
Tuples
  - A tuples are similar to list and can store multiple pieces of data but the data stored in a tuple is immutable, once a tuple is defined it cannot be changed or altered. We define a tuple by using parentheses ( ), tuples are useful when we need to store information that we dont want to change. the code below is an example of a tuple:
```
ben_davies = ("Coderacademy Student", "Programmer", "Full Stack Web Developer")
```


 Dictonaries
  - A Dictonary in Python in great for storing lots of data when we have lots of values we need to keep track of. A piece of data in dictonary contains two pieces of information, these are called keys and values. We define Dictonaries by using Curly Brackets { } See below how we can organise data in a dictonary:
```
ben_davies = {
    "fname": "Ben",
    "lname": "Davies",
    "age": 27,
    "Favourite Food": "Pizza"
}
```

## _Question 5_ 
 Interpreter
  - An Interpreter as the name suggests is a piece of software that can interpret a high level language and convert it into machine code, interpreted languages like Python, Ruby and javascript excute code one statement at a time. Usually interpreter's can anaylze code faster than Compilers but will require more overall time to excute the entire code.

 Compiler
   - A compiler is piece of software that takes a programming language and compiles it into machine code, Compilers will translate an entire program before it can be execute. Usually Compilers will take longer than an interpreter to analyze code as they have to anaylze the entire program, but they make up for it with there quick execution speed.

 Difference
   - Compilers translate the entire code into machine code before a single line is executed, interpreters translate one statement at a time into machine code. 

## _Question 6_
 Python
   - Python is an interpreted High Level object oriented programming language, it is a very flexible language and can used for a variety of applications. It's simple syntax and high level data structures makes it very programmer friendly. Python has a large range of built in modules and packages that allows for quick application development. Because python is an interpreted language it run slower than a programming language like C, also python has high memory consumption making it less preferred for some software Projects. Python despite some of it drawbacks is widely used and some noteable websites such as instragram, netflix, google and spotify all use python as a backend framework to some extent.

 C
  - C is a Programming langauage that was originally developed in 1970's, it's considered a mid level to high level language. C unlike Python isn't a Object Oriented Programming language it is a Procedural Oriented Language. This means C cannot use inheritance prgramming in-turn making reusing your code more difficult. C must be compiled before it can be excuted by the computer. While C has much faster run-times than python it means your code has be compiled before it can be debugged, this leads to longer development times. C dispite its age is still used for many purposes including database like MySQL and Microsoft SQL, langauge compilers, network drivers and utility drivers.

## _Question 7_
 1. access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs
    - Personal Data that can be used to resonably identify someone is subject to the privacy act 1988, an IT professional that has access to personal information is bound by laws of non disclosure. An IT professional should always be working on ways to mitigate cyber threats and safe guard customers personal information. IT professionals can do this by making sure they update all there computers and configure there firewall appropriately to monitor incoming and outgoing traffic, also they should be aware of how they dispose of customers personal information and also make sure senitive data is encrypted. By doing this IT professional can midigate there risk of leaking personal data. The Privacy Act of 1988 details how much and what type of personal data Businesses can store and how to handle personal information. It also explains what steps need to be taken once a customer or users information has been Leaked, altered or lost. Business should also use a variety of strategies and methods to make sure they safe guards users personal information, such as investing in anti-virus software, having a monitoring system for servers and databases, using modern data encryption methods and educating staff and IT professionals on data handling and cybersecurity.

 2. aggressive sales and marketing practices designed to mislead and deceive consumers
    - Online Marketing is in every facit of the internet, Australian consumers are protected by the Consumer Act of 2010. Advertising on the internet is highly regulated by goverment bodies, when a business is marketing thier products or services in a way that is misleading or deceiptive to consumers it is breaking the consumer Act of 2010. although there are some loop holes were companies cannot be held accountable if they don't directly sell and ship there products to australia. Consumers should always be wary when buying from websites that don't have the domain extension of australia ".au". All websites that have the domain extension ".au" are bound by australian consumer law and have a registered australian business number (ABN). An IT professional can follow good marketing practices by reviwing the laws set out in the consumer act of 2010, these include disclosing all hidden fees, giving an accurate discription of goods for sale, deter from using coerceive tactics to urge consumers into purchasing a product and create truthful content and reviews to gain consumer trust.


 #### Optus September Data Leak
  - The optus data leak in september 2022 was one of the most talked about leaks in modern australian history. In september 2022 optus annouced that they had leaking personal data of around 10 millon people, this data included customers names, dates of birth, email addresses, home addresses, driver’s licenses, passport number and Medicare details. It was soon discoved that optus had allowed the attack of there network and there security almost non existant. optus had allow:
    - Allowed a public facing API to access there data servers
    - The API didn't require login credentials or the an authentication protocol
    - Optus stored users data in incrementing order not using a unique string to refernce data

    Optus's lack of oversite on there security made it easy for a hacker to exfiltrate data to external spreadsheet or document. The steps that could have been taken to avoid this, you can regular check your API's to see wether they are public facing and check the authentication protocol is working for them. You can arrange stored users data using unique strings making it harder to hackers for find matching data and also use multi-authenication protocol tools for all API's to improve security. As an IT professional you should always be trying to midigate data breaches immplimenting  and monitoring connections to servers that contain personal and confidential information. One of the best ways to proactively improve data security is to immplement an data access control program in the company to limit the number of people that have permission to access sensitive data. Following this incident optus underwent forceful reviews and regerious overhauleds of it network security. The breach cost the company around 140 million dollars and more importantly there trust and reputation among millions of consumers.

References
- [Privacy Act 1988](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/handling-personal-information/guide-to-securing-personal-information)
- [Consumer Act 2010](https://www.legislation.gov.au/Details/C2023C00449/Html/Volume_4#_Toc152172699)
- [Optus Data Leak](https://www.upguard.com/blog/how-did-the-optus-data-breach-happen)

## _Question 8_
 Python Control Flow
 The control flow of a program is the order in which the lines of code are excuted. There are many types of control flow statements we can write to make our code return the desired outcome. Sequential Control Flow is default for all programs and excutes the code from top to bottom, the list below shows some of the different types of operators we have and how we can use them to write our code.

   - #### Comparison Operators
      - These are at the basis of any control flow statement, like the name suggests comparison operators compare two values and returns a boolean value.Our comparison operators include:
      ```
      "==" : Equal to
      "!=" : Not Equal to
      "<"  : Less than
      ">"  : Greater than
      "<=" : less than or Equal to
      ">=" : Greater than or Equal to
      ```
   - #### Boolean Operators
     - We have three boolean operators in python they are: "and", "or" and "not", these operators check if a condition is true or false and return a boolean value. Below is a diagram of how these operators work and what results they will return when we have >= 1 condition

     ![Boolean Truth Chart](<boolean truth table.jpg>)
    
   - #### Ternary Operators
     - These operators are a combination of Comaparison and Boolean Operators. Ternary Operators are very powerful and are commonlny used when coding, they enable us to shorten our statements and keep our code consise. Below is an example of how ternary operators can make our more DRY.
     ```
     # NO TERNARY OPERATOR
     # GLOBAL VARIABLES

      name = "Ben"
      fav_langauge = "python" 

      if name == "Ben":
          if fav_langauge == "python":
              print(f"{name} is a fullstack Web Developer and loves {fav_langauge}.")
          else:
          print("Not Ben Doesn't love python")
      else: 
          print("Not Ben Doesn't love python")

      # WITH TERNARY OPERATOR
      print(f"{name} is a fullstack Web Developer and loves {fav_langauge}." if name == "Ben" and fav_langauge == "python" else "Not Ben Doesn't love python")

      7 Lines of code shorten into 1 Line of code, much more efficent!
     ```
   - #### If statements
     - if statements are commonly used in conjuction with comparison and boolean operators, if statements allow program to branch into different functions depending on wether the if statement returns a true value or a false one. The if statements in python have three operators they are: "if", "elif", "else" when we write an if statement always finish with colon, we then in python indent the next line of code to specify that it is a block of code. Indentation is required in python but some languages like C and Java use curly brackets instead to indicate a block of code. See Below an example of a simple login program using if statements and a dictonary:
     ```
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
     ```
   - #### LOOPS 
     - Loops are great when we need to excute a piece more than once or interate a code block. We can use loops to search a list or dictonary for specific data, Run a block of code until a certain condition is met or create an infinite loop that can completely break your program. Loops are very great at making our code DRY, there are two types of loops in python they are "while" and "for". A while for will run until the loop statement returns false, in the example above it demonstrates a while loop which give a user 5 attempts to login into there account. For loops are a little more complex than while loops and are used to iterate over a set of data. A block of code can have more than 1 loop, when this happens it is called a nested loop. An example below shows both a while loop with a nested for loop.
     ```
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
     ```

## _Question 9_
  - #### Type Coercion
    - Type Coercion occurs when the programming langauge executes a block of code and the data changes from one type to another type of data. Example a string variable of "2" changes to a integer variable of 2. notice its written in javascript.
      ```
      var x = "2";
      var result = x + 2;
      console.log(result);
      ```
  - #### Type Conversion
    - Type Conversion is the manual conversion of a data type by a programmer, example a string variable of 8 changes to an integer of 8.
    ```
    x = "8"
    print(int(x) + 2)
    ```
    Python doesn't support type Coercion, When writing python programmers must manually change data types if they want to concatinate two pieces of data.
## _Question 10_

  - #### Simple Data Types
    - Simple data types consist of data that only has one value, the simple data types in python include: Strings, Integers, Floats and Booleans. I've written an exmaple of each below.
    ```
    String = "Ben" # Wrapper in quotation marks
    Integer = 2 # Only whole numbers
    Float = 2.48 # Supports both whole and fractional numbers
    Boolean = true or false # Returns a value of true or false 
    ```
  - #### Complex Data Types
    - Complex data types consist of data that can have multiple values, the complex data types in python include: Tuples, Lists, Sets and Dictonaries. I've written an example below.
    ```
    Tuples = ("Hello", "World") # Once defined cannot be changed or altered and is indexed
    List = ["Python", "Html", "Scss", "Javascript"] # Can be changed and is indexed
    set = {"Coder", "Programmer", "Web Dev"} # Cannot contain same value more than once unorder and not indexed
    Dictonary = {"fav_food: "Pizza", "fav_city: "Brisbane"} # contains 2 pieces of data, a key and value 
    ```

## _Question 11_
  - Classes I would create to solve restaurant problem:
    1. class customer_name_and_Location:
       - So that I can reference the cutomer and have the table number the customer is sitting at.
    2. class display_current_menu:
       - So I can update the current menu and allow customers to view my menu and add items to cart.
    3. class cart:
       - So customers can view the list of items before they purchase them.
    4. class payment:
       - Take the payment from the customer.
    5. class order confirmation:
       - This class would send the order to the kitchen and end once the customer recieves the food.

## _Question 12_
```
INCORRECT CODE! 
celsius = input()

fahrenheit = (celsius * 9/5) + 32

print(f"The result is: {fahrenheit}.")
```
The python code will not run because python cannot concatinate a string and an integer. To fix the code so it will perform our desired outcome is to change the value of the variable celsius to an integer, one easy way is to make the variable celsius = integer of the input. See the Correct Code below:
```
celsius = int(input())

fahrenheit = (celsius * 9/5) + 32

print(f"The result is: {fahrenheit}.")
```
## _Question 13_
```
numbers = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0
while (i < len(numbers) - 1) and (numbers[i] < numbers[i+1]):
    i += 1
print(i)

numbers[i] = numbers[i+1]
numbers[i+1] = numbers[i]
```
  - Python cannot swap the elements as we would like in the code above, this is because python excutes the code from top to bottom. On line 280 we specific a new value for the variable numbers[i], we then asign a new value on line 281 to numbers[i+1] = numbers[i]. Therefore we get numbers[i] and numbers[i+1] both being equal to eachother. To make the code execute the way we want it to we need change line 280, python is able to assign multiple variables on the same line we just need to use a comma inbetween them and keep in mind it will asign the variables from left to right. An example of the working code is written below.
```
numbers = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0
while (i < len(numbers) - 1) and (numbers[i] < numbers[i+1]):
    i += 1
print(i)

numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
```
## _Question 14_



## _Question 15_
  - #### Raining Program
    To check if its raining i've written the following pseudo code:
    ```
    # Decare variables raining and cold
    # Get user input is it raining
    # Get user input tempature as an integer
    # IF statement is raining
      # turnary operator for is Cold else hot 
    # else statement
      # turnary operator for is Cold else hot
    ```
## _Question 16_
```
weighted_skills = {
    "python": 1,
    "ruby": 2,
    "bash": 4,
    "git": 8,
    "html": 16,
    "tdd": 32,
    "css": 64,
    "javascript": 128
}
def skill_score():
    print("Welcome to the Coder Skill Score")
    user_input = [input("Please Enter the languages you know \n")]
    user_skills = user_input[0].split(" ")
    
    user_score = 0
    
    print(f"Your skills are: {user_skills}")

    for key, value in weighted_skills.items():
        if key in user_skills:
            user_score = user_score + value
        else:
            continue
    print(f"Your Skill Score is: {user_score} Points\n")

    improvements = {}

    for key, value in weighted_skills.items():
        if key not in user_skills:
            improvements[key] = value
        else:
            continue

    print("To Improve your Skill Score you could learn the follow Programming lanuages")
    for key, value in improvements.items():
        print(f"{key} ':' {value} Extra Points")

skill_score()
```
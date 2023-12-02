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
   - A list in Python is a great way of assigning a variable a value when we have multiple pieces of data we want to store. Within a list we can store both simple data types and complex data types. We define a list by using square brackets [], for example view the code below that conatins Strings an integer and a dictonary:
```
ben_davies = [
    "Male", 27, "Full Stack Developer",
    {
        "favourite Language": "Python",
        "favourite code":"print("Hello World")"
    }
]
```
Tuples
  - A tuples are similar to list and can store multiple pieces of data but the data stored in a tuple is immutable, once a tuple is defined it cannot be changed or altered. We define a tuple with by using parentheses (), tuples are useful when we need to store information that we dont want to change. the code below is an example of a tuple:
```
ben_davies = ("Coderacademy Student", "Programmer", "Full Stack Web Developer")
```


 Dictonaries
  - A Dictonary in Python in great for storing lots of data when we have lots of value we need to keep track of. A piece of data in dictonary contains two pieces of information, these are called keys and values. We define Dictonaries by using Curly Brackets {} See below how we can organise data in a dictonary:
```
ben_davies = {
    "fname" = "Ben",
    "lname" = "Davies",
    "age" = 27,
    "Favourite Food" = "Pizza"
}
```

## _Question 5_ 
 Interpreter
  - An Interpreter as the name suggests is a piece of software that can interpret a low level language or binary and translate it into higher level language that we can understand.

 Compiler
   - A compiler takes a programming language and compiles it into another language, Compilers are nessecary to so we can enter commands that the computer can understand and execute.

 Difference
   - Compilers are used for translating a programming language into another programming language, interpreters are used to translate a lower level language into a higher level language.

## _Question 6_
 Python
   - Python is an interpreted High Level object oriented programming language, it is a very flexible language and can used for a variety of applications. It's simple syntax and high level data structures makes it very programmer friendly. Python has a large range of built in modules and packages that allows for quick application development. Because python is an interpreted language it run slower than a programming language like C, also python has high memory consumption making it less preferred for some software Projects. Python despite some of it drawbacks is widely used and some noteable websites such as instragram, netflix, google and spotify all use python as a backend framework to some extent.

 C
  - C is a Programming langauage that was originally developed in 1970's, it's considered a mid level to high level language. C unlike Python isn't a Object Oriented Programming language it is a Procedural Oriented Language. This means C cannot use inheritance prgramming in-turn making reusing your code more difficult. C must be compiled before it can be excuted by the computer. While C has much faster run-times than python it means your code has be compiled before it can be debugged, this leads to longer development times. C dispite its age is still used for many purposes including database like MySQL and Microsoft SQL, langauge compilers, network drivers and utility drivers.

## _Question 7_
 1. access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs)
    - An It 
    
 2. aggressive sales and marketing practices designed to mislead and deceive consumers



 #### access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs)

References
- [Privacy Act 1998](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/handling-personal-information/guide-to-securing-personal-information)
- jdkfd

## _Question 8_
 Control Flow Python

## _Question 10_
## _Question 11_


## _Question 12_
```
INCORRECT CODE! 
celsius = input()

fahrenheit = (celsius * 9/5) + 32

print(f"The result is: {fahrenheit}.")
```
The python code will not run because python cannot multiple a string by an integer. To fix the code so it will perform our desired outcome is to change the variable celsius to an integer, one easy way is to make the variable celsius = integer of the input. See the Correct Code below:
```
celsius = int(input())

fahrenheit = (celsius * 9/5) + 32

print(f"The result is: {fahrenheit}.")
```
## _Question 13_
## _Question 14_
## _Question 15_
## _Question 16_
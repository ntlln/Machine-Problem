#Allen Caingcoy (INF224)
#Create a program that will ask the user to enter two numbers and choose what operation they want to perform. 
#Then automatically display the result of the operation for the two numbers.
# Use def function in three different approaches:

print("\033[H\033[2J")

# a.Function with no parameter/s
def invalid ():
    print ("\nInvalid Input!")

# b.Function with 2 parameters
def addition (x,y):
    return (x+y)
def subtraction (x,y):
    return (x-y)

# c.Function with 2 parameters and return statement
def multiply (x,y):
    return (x*y)
def divide (x,y):
    return (x/y)
def modulo (x,y):
    return (x%y)

print ("PYTHON CALCULATOR")

print ("\n[+] - Addition \n[-] - Subtraction \n[*] - Multiplication \n[/] - Division \n[%] - Modulo Division")
operation = (input("Chosen Operation: "))

x = int (input("\nEnter First Number: "))
y = int (input("Enter Second Number: "))

if operation == "+":
    print ("")
    print (x, "+", y, "=", (addition(x, y)))
    print ("\nThe sum of these two numbers is:", (addition(x, y)))

elif operation == "-":
    print ("")
    print (x, "-", y, "=", (subtraction(x, y)))
    print ("\nThe difference of these two numbers is:", (subtraction(x, y)))

elif operation == "*":
    print ("")
    print (x, "*", y, "=", (multiply(x,y)))
    print ("\nThe product of these two numbers is:", (multiply(x,y)))

elif operation == "/":
    print ("")
    print (x, "/", y, "=", (divide(x,y)))
    print ("\nThe quotient of these two numbers is:", (divide(x,y)))

elif operation == "%":
    print ("")
    print (x, "%", y, "=", (modulo(x,y)))
    print ("\nAnswer of the two numbers is:", (modulo(x,y)))

else:
    invalid ()
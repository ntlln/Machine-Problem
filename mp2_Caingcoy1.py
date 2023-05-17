#Allen Caingcoy (INF224)
#Using single while loop,create a program that will implement the following output:

print ("\033[H\033[2J")

x = int (input("Starting Number: "))
sn = int (input("Step Number: "))
ln = int (input("Upto What Number? "))
print ()

while x <= ln:
    print (x ** 1)
    x += sn
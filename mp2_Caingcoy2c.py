#Allen Caingcoy (INF224)
#Create a program using nested loop that will output the following on the screen:

print ("\033[H\033[2J")

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("")
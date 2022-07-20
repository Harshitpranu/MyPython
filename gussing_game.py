import random #importing The Random Module
n=random.randint(1,10) #it is a function for creating a random number between ranges

print(n) #you can check the generated random number by this print function
k=n #this variable will hold the generated random number
attempt=5 #this will use how many attempts you have left
for i in range(5): #this loop will hold how many chances you wil give
    a=int(input("enter the number:-")) #loop will execute
    if k==a:
        print("you won")
        break          #if user won this loop will be break
    else:
        print("Try Again!",(attempt-1),"Left")
        attempt=attempt-1 #this is for how many attempts you have left


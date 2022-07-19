import random
n=random.randint(1,10)
print(n)
k=n
attempt=5
for i in range(5):
    a=int(input("enter the number:-"))
    if k==a:
        print("you won")
        break
    else:
        print("Try Again!",(attempt-1),"Left")
        attempt=attempt-1


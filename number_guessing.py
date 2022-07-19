import random
n = random.randint(0,10)
k=n
for i in range(5):
    a = int(input('Enter Number: '))
    if a==k:
        print('You won!')
        break
    else:
        print("Try again!")


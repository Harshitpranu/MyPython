n=int (input("enter any Number"))
rn=0
while n>0:
    remainder=n%10
    rn=rn*10+remainder
    n=n//10

print("the reverse number=",rn)




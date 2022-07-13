n=int (input("enter Any Number"))
sum=0
while n>0:
    remainder=n%10
    sum=sum+remainder
    n=n//10
print("sum of Digits is=",sum)
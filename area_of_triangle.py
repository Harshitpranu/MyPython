a=int (input("Enter a"))
b=int (input("Enter b"))
c=int (input("Enter c"))
s=int ((a+b+c)/2)
print("s=",s)
import math

area=float (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("Area=",area)

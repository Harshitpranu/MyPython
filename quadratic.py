a=int (input("Enter The Value Of a"))
b=int (input("Enter The value Of b"))
c=int (input("Enter The value of c"))
D=int(b**2)-int(4*a*c)
print("D=",D)
if D>0:
    print("equation has two real and different roots ")
elif D<0:
        print("equation has two complex roots")
else:
    print("equation has only one real root")
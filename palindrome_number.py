n = int(input("enter any Number"))
i=n
rn =0
while n > 0:

    remainder = n % 10
    rn = rn * 10 + remainder
    n = n // 10
print("the reverse number=", rn)
if i==rn:
    print("this is a palindrome number")
else:
    print("not a palindrome number")

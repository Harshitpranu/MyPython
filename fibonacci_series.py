nterm=int (input("how many terms"))
n1=0
n2=1
i=0
while i<nterm:
    print(n1," ",end="")
    n=n1+n2
    n1=n2
    n2=n
    i=i+1

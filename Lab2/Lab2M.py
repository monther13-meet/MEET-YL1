def monder(n):
    for i in range(1,n+1):
        if n%i==0:
            print i
s=int(raw_input("enter a number:"))
monder(s)


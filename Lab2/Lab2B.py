import random
def mon():
    while True :
        n = raw_input("n")
        if n == "n":
            x = float(raw_input("Enter a number between 0 and 1"))
            if x>0 and x<0.5:
                print "h"
            if x<1 and x>0.5:
                print "t"
            if x==0.5:
                print "fair"
mon()

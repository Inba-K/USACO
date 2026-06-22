def cowllatz(x,j):
    while x>=1:
        if x==1:
            return 1
        elif x%2==0:
            x=x/2
        else:
            x=x*3+1
        j+=1
    return j
print(cowllatz(int(input()),0))

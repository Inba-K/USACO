def cowllatz(x):
    j=0
    while x>1:
        if x%2==0:
            x/=2
        else:
            x=x*3+1
        j+=1
    return j

print(cowllatz(int(input())))
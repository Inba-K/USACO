import random
def steal(lis):
    lis.sort()
    for i in range(1,len(lis)):
        if lis[i]-lis[i-1]==2:
            return lis[i]+1
    return -1

x=int(input())
y=int(input())
lis=list(range(x,y+1))
random.shuffle(lis)
lis.pop()
print(steal(lis))
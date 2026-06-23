r=int(input())
p=int(input())
order=list(range(1,p+1))

for i in range(1,r+1):
    if i%2==0:
        for j in range(0,p,2):
            order[j-1],order[j]=order[j],order[j-1]
    else:
        for k in range(0,p-1,2):
            order[k],order[k+1]=order[k+1],order[k]

print(order)
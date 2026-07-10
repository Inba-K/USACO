def picture(m,n,g,h,k):
    for i in range(m):
        for j in range(n):
            k.append(abs(g[i]-h[j]))
    k.sort()
    return k[0]
m,n=map(int,input().split())
g=list(map(int,input().split()))
h=list(map(int,input().split()))
k=[]
print(picture(m,n,g,h,k))
from itertools import product
def Cowstring(N,forbid,letters):
    cowstring=[''.join(item) for item in product(letters,repeat=N)]
    result=len(cowstring)
    for i in range(len(cowstring)):
        if forbid in cowstring[i]:
            result-=1
    return result

letters=['C','O','W']
N,forbid=input().split()
N=int(N)
print(Cowstring(N,forbid,letters))
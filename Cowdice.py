a=0
for i in range(1,5):
    for j in range(1,7):
        if j>=i:
            for k in range(1,9):
                if k>=j:
                    for l in range(1,11):
                        if l>=k:
                            for m in range(1,13):
                                if m>=l:
                                    for n in range(1,21):
                                        if n>=m:
                                            a+=1
                                            print(i,j,k,l,m,n)

print("Bessie can win in",a,"ways.")
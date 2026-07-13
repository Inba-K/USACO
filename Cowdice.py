a=0
for i in range(1,5):
    for j in range(1,7):
        if i>j:
            break
        for k in range(1,9):
            if j>k:
                break
            for l in range(1,11):
                if k>l:
                    break
                for m in range(1,13):
                    if l>m:
                        break
                    for n in range(1,2):
                        if m>n:
                            break
                        else:
                            a+=1

print("Bessie can win in",a,"different ways.")
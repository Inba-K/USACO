def MOOdoku(str1,str2,str3,str4,str5,str6,M):
    for i in range(6):
        if str1[i]=='M':
            M+=1
        elif str2[i]=='M':
            M+=1
        elif str3[i]=='M':
            M+=1
        elif str4[i]=='M':
            M+=1
        elif str5[i]=='M':
            M+=1
        elif str6[i]=='M':
            M+=1
        if M>2:
            M=0
            return 0
        else:
            return "Good"
        

str1=input().split()
str2=input().split()
str3=input().split()
str4=input().split()
str5=input().split()
str6=input().split()
M=0
print(MOOdoku(str1,str2,str3,str4,str5,str6,M))
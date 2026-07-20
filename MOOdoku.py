def MOOdoku(str1,str2,str3,str4,str5,str6,M,M1):
    for i in range(0,5):
        
        for j in str_list:
            if j[i]=='M':
                M1+=1
                if M1>2:
                    return 0

        
        

str1=input().split()
str2=input().split()
str3=input().split()
str4=input().split()
str5=input().split()
str6=input().split()
M=0
M1=0
str_list=[str1,str2,str3,str4,str5,str6]
print(MOOdoku(str1,str2,str3,str4,str5,str6,M))
Naive String MAtching Algorithm
str1 = "Hello Worllod"
str2 = "llo"

for s in range(0,len(str1)-len(str2)+1):
    j = 0
    lengthPattern=0
    for i in range(len(str2)):
        if str2[i] == str1[s+j]:
            lengthPattern+=1
            j+=1
    if lengthPattern == len(str2):
        print("Pattern do exist!")

Rabin-Karp String MAtching Algorithm
str1 = "2689145"
str2 = "89"
#
d = 10
q = 11
m = len(str1)
n = len(str2)
hashConst =  int((d**(n-1))%q)
patternHash = 0
stringWindowHash = (m-n)*[0]

for i in range(n):
    patternHash = int(d*patternHash + int(str2[i]))%q
    stringWindowHash[0] = int(d*stringWindowHash[0] + int(str1[i]))%q

for s in range(0,m-n):
    if(patternHash == stringWindowHash[s]):
        length = 0
        for i in range(n):
            if(str2[i] == str1[s+i]):
                length+=1
        if(length == n):
            print("Pattern does exist")
    else:
        try:
            stringWindowHash[s+1] = int(d*(stringWindowHash[s]-(int(str1[s])*hashConst)) + int(str1[s+n]))%q
        except:
            pass

print(stringWindowHash)

#EUCLID
# a = 60
# b = 24
#
# while(True):
#     if b == 0:
#         print("GCD",a)
#         break;
#     else:
#         r=a%b;
#         a=b
#         b=r

# Consecutive Integer Checking algorithm
# a = 60
# b = 120
# x = min(a,b)
# while True:
#     if a%x == 0:
#         if b%x == 0:
#             print("GCD",x)
#             break
#         else:
#             x=x-1
#     else:
#         x=x-1

import math
str1 = "AbcDegPs"
dynamicPrimeList = []
m = len(str1)
for i in range(m):
    # if ord(str[i]) is prime... fine
    # if not then make is closest prime either to left or right side
    if str1[i] not in dynamicPrimeList:
        count = 0
        for j in range(2,math.sqrt(ord(str1[i]))+1):
            if ord(str1[i])%j == 0:
                count+=1
        if(count!=0):
            #Prime
            #We dont have to alter this ascii char in
            # input string
            dynamicPrimeList.append(str1[i])
        else:

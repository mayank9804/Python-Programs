# Rabin-Karp String MAtching Algorithm
str1 = "2689145"
str2 = "89"
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

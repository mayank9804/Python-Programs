
#EUCLID

a = 60
b = 24

while(True):
    if b == 0:
        print("GCD",a)
        break;
    else:
        r=a%b;
        a=b
        b=r

# Consecutive Integer Checking algorithm
a = 60
b = 120
x = min(a,b)
while True:
    if a%x == 0:
        if b%x == 0:
            print("GCD",x)
            break
        else:
            x=x-1
    else:
        x=x-1

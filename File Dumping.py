
from pickle import *
f = open("abc.pck","wb")

dump([1,2,3],f)
dump({1:0,2:1,3:2,4:3},f)
dump((1,2),f)
f.close()
f = open("abc.pck","rb")
while True:
    try:
        item = load(f)
        print(item)
    except:
        break

f.close()

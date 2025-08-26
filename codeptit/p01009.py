s = input()
t =[]
h = []
#hoăc t = h = list()
ct=ch=0
for x in s:
    if 'a' <= x <= 'z' :
        ct+=1
        t.append(x)
        h.append(chr(ord(x)-32))
    elif 'A' <= x <= 'Z':
        ch+=1
        t.append(chr(ord(x)+32))
        h.append(x)
    else :
        t.append(x)
        h.append(x)

if ct>=ch: 
    print(*t,sep="")
else:
    print(*h,sep="")

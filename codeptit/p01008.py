s = input()
for x in s:
    if 'a' <= x <= 'z' :
        print(chr(ord(x)-32), end="")
    else : print(x,end="")
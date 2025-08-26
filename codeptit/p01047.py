import math
t = int(input())
def nt(s):
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0 : return False
    return s>1

for _ in range(t):
    n = input()
    tmp = int(n[-4:])
    if nt(tmp): print("YES")
    else : print("NO")

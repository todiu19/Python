def nt(a):
    for i in range(2,int(a**0.5+1)):
        if a%i == 0: return False
    return a>=2

import math
t = int(input())
for _ in range(t):
    a = int(input())
    cnt = 0
    # print(nt(a))
    for i in range(a):
        if math.gcd(i,a)==1 : cnt+=1
    if nt(cnt) : print("YES")
    else : print("NO")

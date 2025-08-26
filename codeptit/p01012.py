t = int(input())
import math
def nt(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 : return False
    return n>1

for _ in range(t):
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    cnt = 0
    while c>0:
        cnt += c%10
        c//=10
    if nt(cnt) : print("YES")
    else : print("NO")
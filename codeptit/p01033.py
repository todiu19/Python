from math import*
l,r = map(int,input().split())
for a in range(l,r-1):
    for b in range(a+1,r):
        for c in range(a+2,r+1):
            if gcd(a,b)==1 and gcd(b,c)==1 and gcd(c,a)==1:
                print(f"({a}, {b}, {c})")
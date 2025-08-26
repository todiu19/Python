from math import*
t = int(input())
for _ in range(t):
    n1 = input()
    n2 = int(n1[::-1])
    n1 = int(n1)
    if gcd(n1,n2) == 1: print("YES")
    else : print("NO")
from math import*
t = int(input())

for _ in range(t):
    s1 = input()
    s2 = s1[::-1]
    k = 0
    for i in range(1,len(s1)):
        if fabs(ord(s1[i]) - ord(s1[i-1])) != fabs(ord(s2[i]) - ord(s2[i-1])) :
            print("NO")
            k=1
            break
    if k == 0: print("YES")
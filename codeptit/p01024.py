from math import*
t = int(input())
for _ in range(t):
    n = input()
    cnt = int(n[-1])
    check = 1
    for i in range(len(n)-1):
        cnt +=int(n[i])
        if fabs(int(n[i]) - int(n[i+1]))!=2 :
            check = 0
            break
    if check and cnt %10 ==0 : print("YES")
    else : print("NO")
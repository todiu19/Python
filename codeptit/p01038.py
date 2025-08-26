t = int(input())

for _ in range(t):
    cnt = 0
    sum = 0
    n = input()
    sum+=int(n)
    while cnt < 1000:
        if sum%7==0 :
            print(sum)
            break
        sum = str(sum)
        x = int(sum[::-1])
        sum = int(sum)
        sum+=x
        cnt+=1
    if cnt==1000: print(-1)
        

n,k = map(int,input().split())
import math
cnt = 0
for i in range(10**(k-1),10**k):
    if math.gcd(n,i) == 1:
        cnt+=1 
        print(i,end=" ")
        if cnt == 10 : 
            print()
            cnt = 0
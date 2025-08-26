t = int(input())
for _ in range(t):
    n = int(input())
    print("1",end=" ")
    for i in range(2,int(n**0.5)):
        cnt = 0
        while n%i == 0 :
            cnt+=1
            n//=i
        if cnt : 
            print(f" * {i}^{cnt} ",end="")  
        
    if n > 1 : 
        print(f" * {n}^{1}",end="")
    print()  
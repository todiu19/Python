x = int(input())
for _ in range(x):
    n = input()
    k = 0
    for i in range(len(n) - 1):
        if n[i] > n[i+1]: 
            print("NO")
            k=1
            break
    if not k : print("YES")
    
    
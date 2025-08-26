tc = int(input())
for _ in range(tc):
    n = input()
    ch = True
    for x in n:
        if int(x) != 4 and int(x) != 7 : 
            ch = False
            print("NO")
            break
    
    if ch : print("YES")

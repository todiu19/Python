n,m = map(int,input().split())
a = n
while n>0:
    if n ==1 or n == a:
        for i in range(m):
            print("* ",end = "")
    else : 
        for i in range(m):
            if i == 0 or i== m-1:
                print("* ",end= "")
            else : print("  ",end= "")
    print()
    n-=1
        
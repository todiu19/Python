n,m,h = map(int,input().split())
a = h
if (m-n)%2!=0 or (m-n)/2!= h-1 : 
    print("NO")
else:
    while h > 1:
        for i in range(h-1):
            print ("  ",end="")
        if h == a :
            print ("* "*n,end="")
        else:
            for j in range(2*h - 2,m*2):
                if j == 2*h - 2 or j == 2*m - 2*h - 1:
                    print("* ",end="")
                else : print(" ",end= "")
        print()
        h-=1

    for i in range(m):
        print("* ",end="")
    

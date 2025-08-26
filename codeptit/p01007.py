t = int(input())
for _ in range(t):
    n,x,m = map(float,input().split(" "))
    year = 0
    while year >=0  and n < m :
        n += (x*n)/100
        year +=1
    print(year)
t = int(input())
for _ in range(t):
    n = int(input())
    factor = 10
    while n >=factor:
        x = n % factor
        if x >= factor/2 :
            n += (factor - x)
        else:
            n -= x
        factor*=10
    print(n)

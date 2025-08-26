    # Smallest Prime Factor
    # Largest Prime Factor
# Sàng
a = [0] * (200000+1)
a[0] = 0
a[1] = 1
for i in range(2,200001) :
    if a[i] == 0:
        for index in range(i*i,200000,i):
            # if a[index] ==0: neu là spff
            a[index ] = i

for i in range(2, 200001):
    if a[i] == 0 :
        a[i] = i    
pt = int(input())
for _ in range(pt):
    n = int(input())
    print(a[n])


a, k, n = map(int, input().split())

b = (-a) % k # 

if b == 0:
    b = k

if b > n - a:
    print(-1)

while b <= n - a:
    print(b, end=" ")
    b += k

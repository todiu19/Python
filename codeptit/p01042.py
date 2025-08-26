t = int(input())
for _ in range(t):
    s = input()
    if any(ch in s for ch in ['3', '4', '5','6','7','8','9']):
        print("NO")
    else : print("YES")

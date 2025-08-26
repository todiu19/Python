t = int(input())
for _ in range(t):
    s = input()
    s1 = s[0]
    s2 = s[1]
    if s1 == s2 : 
        print("NO")
        break
    check = 1
    for i in range(2,len(s)):
        if i % 2 == 0 and s[i] != s1:
            check = 0
            break
        if i%2 ==1 and s[i]!=s2:
            check = 0
            break
    if check == 1:
        print("YES")
    else : print ("NO")
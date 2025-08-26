t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)):
        if 'A'<=s[i]<='Z' : 
            print(s[i],end="")
        elif '0' <= s[i] <= '9' : 
            for x in range(1,int(s[i])):
                print(s[i-1],end="")
        else : print(s[i],end="")
    print()
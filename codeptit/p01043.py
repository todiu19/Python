t = int(input())
def check(s):
    for i in s:
        if int(i)%2==1:
            return False
    return True
a=[]
b=[]
num = 2

while num <=888:
    if check(str(num)):
        tmp = str(num)
        a.append(tmp+tmp[::-1])
        b += (tmp + tmp[::-1])
    num+=2
for _ in range(t):
    n = int(input())
    for i in a:
        if int(i) >= n:
            break
        print(i,end=" ")
    print()


    
t = int(input())
def nt(x):
    for i in range(2,int(x**0.5)+1):
        if x%i ==0 : return False
    return x>1

for _ in range(t):
    n = input()
    if not nt(len(n)):
        print("NO")
        continue
    # cntnt = n.count('3')+n.count('7')+n.count('5')+n.count('2')
    # cnt = n.count('0')+n.count('1')+n.count('4')+n.count('6')+n.count('8')+n.count('9')
    cntnt = 0
    cnt =0
    for x in n:
        if x in "2357":
            cntnt+=1
        else : cnt+=1
    if cntnt <= cnt :
        print("NO")
        continue
    else : print("YES")
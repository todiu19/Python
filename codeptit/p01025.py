s1= input()
list1 = []
i = 0
cnt = 0
s = s1[::-1]
for i in s:
    if cnt == 3 :
        cnt = 0
        list1 +=','
    list1+=i
    cnt+=1
list1.reverse()
print(*list1,sep='')

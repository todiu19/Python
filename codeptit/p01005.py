n = input()
cf = cs = 0
for x in n:
    if int(x) == 4 : cf +=1
    if int(x) == 7 : cs +=1
if cf + cs == 4 or cf + cs == 7 : print("YES")
else : print("NO")
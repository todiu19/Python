s = int(input())
from collections import Counter
for x in range(3,s+1):
    a = ["" for _ in range(x)]
    def check():
        fred = Counter(a)
        if fred['A'] <= fred['B'] <= fred['C'] and fred['A'] >0 and fred['B']>0 and fred['C']>0 :
            result()
    def result():
        for i in range(x):
            print(a[i],end="")
        print()

    def Try(i):
        for j in "ABC":
            a[i] = j
            if i==x-1:
                check()
            else : Try(i+1)
    Try(0)
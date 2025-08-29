s = input()
for x in s:
    if 'a' <= x <= 'z' :
        #ord(x) laays mã ascii
        print(chr(ord(x)-32), end="")
    else : print(x,end="")


s = input()
if s[:2] == s[(len(s)-2):] : print("YES")
else : print("NO")

#chuyen number to string
s = str(100)

s = "  python programming  "

print(s.upper())      # PYTHON PROGRAMMING
print(s.lower())      # python programming
print(s.strip())      # bỏ khoảng trắng 2 đầu
print(s.replace("python", "java"))  # java programming
print(s.split())      # ['python', 'programming']
print("-".join(["A", "B", "C"]))    # A-B-C

text = "Hello Python"
print(text.find("Python"))   # 6
print("86123486".rfind("86")) # 6
print(text.find("Java"))     # -1
print(text.count("Python")) #đếm số lần xuất hiện xâu con ko chồng lấn
import re
matches = re.findall(f"(?={'Python'})", text) # số lần xuất hiện xâu con chồng lấn. 
#return list cacs vij tri>
# soos xaau con chong lan = len(matches)
if text.endswith("Python") : print("YES")


## đếm ký tự:
s = "Hello_World"
# Đếm từng ký tự:
print(s.count("l"))
# Đếm tất cả ký tự
from collections import Counter
list4 = Counter(s)
print(list4)


''' Hàm Kiểm tra kí tự'''
# Kiểm tra từng yêu cầu
print(any(c.isalnum() for c in s))   # Dòng 1: có ký tự chữ hoặc số
print(any(c.isalpha() for c in s))   # Dòng 2: có ký tự chữ
print(any(c.isdigit() for c in s))   # Dòng 3: có chữ số
print(any(c.islower() for c in s))   # Dòng 4: có chữ thường
print(any(c.isupper() for c in s))   # Dòng 5: có chữ hoa
# Căn giữa, trái, phải cho chuỗi
# .center(15,'-'), .ljust(15,"-"), .rjust(15,"-")

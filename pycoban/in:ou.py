#INPUT
name = input()  # Nhập chuỗi


age = int(input("Nhập tuổi: "))      # Số nguyên
height = float(input("Nhập chiều cao: "))  # Số thực
## import sys : toocs ddooj cao hon input()
import sys
t = int(sys.stdin.readline())
# Nhập 3 số cách nhau bởi khoảng trắng
a, b, c = map(int, input().split())
# .split() → tách chuỗi theo khoảng trắng.
# map(int, ...) → chuyển từng phần tử sang số nguyên.


#OUTPUT

print("Xin chào", name)

#Cách nhau bởi dấu cách (mặc định)
print(a, b, c)  # 1 2 3

# Không có dấu cách hoặc dùng định dạng:
print(a, b, c, sep="-")  # 1-2-3

# Kết hợp f-string (Python ≥3.6)
print(f"Tuổi: {age}, Chiều cao: {height}")

# Không xuống dòng (mặc định print() kết thúc bằng newline)
print(a, end=" ")
print(b)

number = 3.1415926535
print(f"so thuc 4so sau,:{number:.4f}")
print("so thuc 4so sau,:{:.4f}".format(number))

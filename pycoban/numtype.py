a = 4 # integer a = 4
print(a)
b = 10.1241 #float
print(b) #chỉ in 15 số

#kieu Decimal
# lấy toàn bộ nội dung của thuư viện decimal
from decimal import*

#lấy tối đa 30 chữ số nguyen và phần thập phân
getcontext().prec = 30 # só luonnwj số in ra mong muốn
print(Decimal(10)/Decimal(3))
d = Decimal(10)/Decimal(3)
print(type(d))

#kieu phan so
# import thuw vien 
from fractions import*

f1 = Fraction(6,9) #phan so tu rut gon
print(f1)
f2 = Fraction(5,10)
print(f1,"+",f2,"=",f1+f2)
print(type(f1))

#kieu soo phuc _ complex
c = complex(2,5)
print(c)
print(c.real)
print(c.imag)



x = 3.14159

print(f"{x:.2f}")  # làm tròn 2 chữ số thập phân → 3.14
print(f"{x:.4f}")  # làm tròn 4 chữ số thập phân → 3.1416

x = 3.14159
y = round(x, 2)  # làm tròn 2 chữ số thập phân
print(y)          # 3.14
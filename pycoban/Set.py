''' SET
Không chứa phần tử trùng lặp.
Không có thứ tự (unordered).
Có thể thay đổi (mutable) nhưng chỉ chứa được các phần tử bất biến (immutable) như int, str, tuple (không chứa được list hoặc dict).
'''
# Tạo set từ dấu ngoặc nhọn {}
my_set = {1, 2, 3, 4, 4}
# note: {} là dict rỗng, không phải set.
# Muốn tạo set rỗng phải dùng set().
print(my_set)   # {1, 2, 3, 4} (tự loại bỏ phần tử trùng lặp)

# Tạo set từ hàm set()
another_set = set([1, 2, 3, 2])
print(another_set)  # {1, 2, 3}

s = {1, 2, 3}

""" Method"""
# Thêm phần tử
s.add(4)
print(s)  # {1, 2, 3, 4}

# Xóa phần tử
s.remove(2)   # Xóa 2, nếu không có thì báo lỗi
print(s)      # {1, 3, 4}

s.discard(5)  # Xóa 5, nếu không có thì KHÔNG báo lỗi
print(s)      # {1, 3, 4}

# Lấy phần tử bất kỳ và xóa khỏi set
print(s.pop())  # Ví dụ: 1
print(s)        # {3, 4}

# Xóa hết phần tử
s.clear()
print(s)  # set()

"""Các phép toán tập hợp"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Hợp
print(a | b)   # {1, 2, 3, 4, 5, 6}
print(a.union(b))
# Giao
print(a & b)   # {3, 4}
print(a.intersection(b))
# Hiệu
print(a - b)   # {1, 2}
print(a.difference(b))
# Hiệu đối xứng (phần tử thuộc 1 trong 2 set, nhưng không thuộc cả hai)
print(a ^ b)   # {1, 2, 5, 6}
print(a.symmetric_difference(b))


""" Các thao tác thay đổi set"""
a.update(b)  or a |=b
a.intersection_update(b) or a &= b 
a.difference_update(b) or a-=b
a.symmetric_difference_update() or a^=b
# set2
# tương tự như các phép giao hơp hiệu hiệu đối xứng

''' So sanh 2 set'''
A = {1, 2, 3}
B = {1, 2, 3}
C = {1, 2}
#So sánh bằng & khác
print(A == B)   # True  (tập hợp bằng nhau)
print(A != C)   # True  (khác nhau)
#Quan hệ tập con (subset)
print(A < B)          # True  (A là tập con thực sự của B)
print(A <= B)         # True  (A là tập con hoặc bằng B)
print(A.issubset(B))  # True tương đuongư với a<=b 
#Quan hệ tập cha (superset)
print(B > A)            # True  (B là tập cha thực sự của A)
print(B >= A)           # True  (B là tập cha hoặc bằng A)
print(B.issuperset(A))  # True b>=a
#Kiểm tra giao nhau
print(A.isdisjoint(C))   # True (không có phần tử chung)
print(A.isdisjoint({2, 3})) # False (có phần tử chung = 2)
#Các phép toán quan hệ tập hợp
print(A | B)  # Hợp: {1, 2, 3, 4, 5}
print(A & B)  # Giao: {3}
print(A - B)  # Hiệu: {1, 2}
print(A ^ B)  # Đối xứng: {1, 2, 4, 5}


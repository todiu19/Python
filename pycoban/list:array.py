#Acess list
numbers = [1, 2, 3, 4, 5]   # mảng số nguyên
fruits = ["apple", "banana", "mango"]  # mảng chuỗi
mixed = [1, "apple", 3.5, True]        # mảng hỗn hợp
list1 = list() 
list2 = []

#truy cập phần tử: index bắt đầu từ 0
print(fruits[0])  # apple
print(fruits[2])  # mango
print(fruits[-1]) # mango

# change phần tử
fruits[0] = "orange"
fruits[1:3] = ['banana','lemon']
print(fruits)  # ['orange','banana','lemon']

# Nối chuỗi
fruitsx = ['apple','mango','watermelon']
fruits += fruitsx # hoac fruits.extend(fruitsx)

print(fruits)

#duyệt list:
print(fruits[1:2],fruits[-3:-1]) #['orange', 'mango'] ['apple', 'orange', 'mango']
for fruit in fruits:
    print(fruit)

# Check if item exits 
if 'orange' in fruits: print("Yes")

# METHOD
fruits.append("grape")   # thêm vào cuối
fruits.reverse()         # dao nguoc chuoi = fruits[::-1]
fruits.insert(1, "kiwi") # chèn tại vị trí 1
fruits.remove("apple")   # xóa theo giá trị
fruits.pop(2)            # xóa theo chỉ số, pop() method removes last item
print(len(fruits))       # độ dài mảng
#Copy list
fruits2 = fruits.copy()  # tao lisst moi giong list hien tai
fruits3 = list(fruits2)
fruits4 = fruits3[:]

#Sort
fruits.sort()            # sắp xếp mảng tang
print(fruits)
fruits.sort(reverse = True)
print(fruits)

# list comprehension offers a shorter syntax (cus phap nganws hon) when yu want to create a new list based on (dựa trên) values of existing list
newlist = [x for x in fruits if "a" in x]
# [expression 'for' item 'in' iterable 'if' condition == True]
# nếu tạo 2 list từ 2 đk if else thì cos thẻ dùng 2 lầncách trên hoặc:
newlist1=[]
newlist2=[]
[newlist1.append(x) if 'a' in x else newlist2.append(x) for x in fruits]
print(newlist,newlist1,newlist2)

#
#thư viện array
import array
arr = array.array('i', [1, 2, 3])  # 'i' = kiểu int
print(arr)
print(list(arr))
# In ra mảng mà không có ngoặc và dấu phẩy
print(*arr)
# In chuỗi mà không có ngoặc , dấu phẩy và dấu cách
lst = [1, 2, 3, 4]
print(*lst, sep='')   # 1234



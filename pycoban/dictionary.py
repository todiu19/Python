"""
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not
allow duplicates.
"""
#### initialize 
#c1
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
#c2
car = {}
car["g63"] = "mec"
car["lexus"] = "toyota"

# c3
person = dict(name="Tran Van B", age=22, city="HCM")


print(student["name"]) 
print(student.get("age")) # tuongw duong voiw trene nhma ko bao loi khi age ko ton tai

## keys() method
# Returns a dict_keys object
print(student.keys())          # dict_keys(['name', 'age', 'grade'])

# Looping through keys
for k in student.keys():
    print(k,student[k])

# Converting to list
keys_list = list(student.keys())
print(keys_list)               # ['name', 'age', 'grade']


## Remove Dictionary Items

student.pop("age") #Xoa age : 20
student.popitem() # remove last item
student.clear() # Xoa sach

###Loop through Dictionary
# in ra cacs keys giống như for person.keys()
for x in person: 
    print(x,end = " ")
print()
for x in person.values():
    print(x,end=" ")
print()
for x in person:
    print(person[x],end=" ")
print()
for x, y in person.items():
    print(x,y,end=" ")
print()

##Copy dict
newdict = person.copy()
newdict2 = dict(person)
print(newdict2)

# update()
person.update({"city": "Da Nang", "age": 22})
person["city"] = "Ha Noi"
print(person)

###Nested Dict 
# Khởi tạo nested dictionary
students = {
    "sv1": {
        "name": "Nguyen Van A",
        "age": 20,
        "major": "IT"
    },
    "sv2": {
        "name": "Tran Thi B",
        "age": 21,
        "major": "Math"
    },
    "sv3": {
        "name": "Le Van C",
        "age": 19,
        "major": "Physics"
    }
}
# hoac co ther khai bao tungwf dict con rooif khai bao dict tong
'''
student = {
    "sv1" = sv1
    "sv2" = sv2
    "sv3" = sv3
}
'''
# Truy cập vào nested dict
print(students["sv1"]["name"])   # Nguyen Van A
print(students["sv2"]["age"])    # 21

# Duyệt toàn bộ nested dictionary
for key, info in students.items():
    print(f"ID: {key}")
    for k, v in info.items():
        print(f"   {k}: {v}")

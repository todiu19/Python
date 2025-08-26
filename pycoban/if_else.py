s = "hello banana"

#kiem tra 1 xaau/kytu có thuoc string hay ko
if "a" in s: print("a cos trong s")

# kiểm tra nhiều ký tự
if any(x in s for x in ['a', 'b', 'c']):
    print("Có ít nhất một ký tự a/b/c trong chuỗi")
if all(x in s for x in ['a', 'b']):
    print("Có cả a và b trong chuỗi")

# hoac dung set
s = "banana"
chars = {'a', 'b', 'c'}

if set(s) & chars:
    print("Có ít nhất 1 ký tự trong {'a','b','c'}")

if chars <= set(s):
    print("Chuỗi chứa đầy đủ a, b, c")



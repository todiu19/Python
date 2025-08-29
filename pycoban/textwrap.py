thickness = int(input())  # This must be an odd number
c = 'H'

# Top cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))  

# Bottom pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))  

# Bottom cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

import textwrap
text = "Python is an amazing programming language."
width = 10
textwrap.wrap(text, width )
# Chia một chuỗi dài text thành một danh sách các chuỗi con, mỗi chuỗi con có độ dài tối đa width.

textwrap.fill(text, width )
# Trả về chuỗi mới đã được xuống dòng tự động sao cho mỗi dòng không vượt quá width.

textwrap.indent(text, prefix =10)
# Thêm tiền tố prefix vào đầu mỗi dòng của chuỗi.

textwrap.dedent(text)
# Loại bỏ khoảng trắng thừa ở đầu các dòng, thường dùng khi copy code nhiều dòng.
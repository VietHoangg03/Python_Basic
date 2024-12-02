"""
Biến trong python
- Trong python thật sự thì không có hằng số vì thay đổi bất kì lúc nào
- Tường khai báo và gán trong một modun và người dùng hạn chế không
thay đổi giá trị của nó. Ở đây, mô-dun là một tệp mới chứa các biến,
hàm,.. được nhập vào tệp chính. Bên trong môddun các hằng số được 
viết bằng tất cả các chữ cái in hoa và dấu gạch dưới ngăn cách
các từ.
"""

x = 5
print(x)

y =15
y=10
print(y) #In ra giá trị sau cùng

x, y, z = 1, 2, "Xin chào" #Gắn nhiều biến cùng lúc
print(x)
print(y)
print(z)

x = y = z ="HOÀNG" # Gắn nhiều biến một giá trị
print(x)
print(y)
print(z)


PI = 3.14
print(PI)

PI = 3.1415
print(PI)


import math
print(math.pi)
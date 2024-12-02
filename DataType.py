"""
Python ngôn ngữ chạy thông dịch, không cần biên dịch ra mã máy để 
thực thi luôn.
Nó tự đoán kiểu dữ liệu động, do trình thông dịch làm thông qua giá
trị của biến là gì.
ví dụ x =  1 => int
x = 1.0 => float
x = 1 + 2 => complex (số phức)
x = true => bool
x = 'abc' => str
x = none => NoneType chỉ ra giá trị null

=> không cần khai báo kiểu dữ liệu

Ưu điểm: Viết mã nhanh hơn, ít mã hơn
Nhược điểm: thời gian chạy lâu hơn, khả năng xảy ra lỗi khó gỡ lỗi


Kiểm tra kiểu dữ liệu : type(tên biến);
"""


x = 1
print(type(x))

x = 1.0
print(type(x))

x = 1 + 2
print(type(x))

x = "abc"
print(type(x))

x = None
print(type(x))
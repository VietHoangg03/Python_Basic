"""
Là một chuỗi các phần tử có thứ tự giống List. Sự khác biệt duy nhất là
bộ giá trị là hằng số. Tuples một khi được tạo ra thì giá trị của
nó không thể sửa đổi.

Tuples được sử dụng để bảo vệ dữ liệu và thường nhanh hơn danh sách
vì chúng không thể thay đổi động.

Được định nghĩa trong dấu ngoặc đơn (), các mục được phân tách bằng dấu phẩy.

Giá trị của Tuple có thể bị trung lặp
"""

gioiTinh = ("Nam", "Nữ")

traiCay = ("Táo", "Chuối", "Cam", "Mận", "Dưa hấu", "Táo")

print(gioiTinh[0])
print(gioiTinh[1])

print(traiCay)

#Cộng hai tuple
y = gioiTinh + traiCay
print(y)

#Kiểm tra 
print("Táo" in traiCay) #True and False

# Độ dài
x = len(traiCay)
print(x)

# Đếm số lượt xuất hiện
print(traiCay.count("Táo"))

# Tìm min max và tính sum
print(min(traiCay))
print(max(traiCay))


# Sắp xếp và chuyển về List
listTC = sorted(traiCay)
print(listTC)
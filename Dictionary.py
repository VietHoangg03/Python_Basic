"""
Từ điển được sử dụng để lữu trữ cá giá trị dữ liệu trong cặp Key:value
Từ điển là một tập hợp được sắp sếp theo thứ tự, có thể thay đổi và ko 
trùng lặp
Sử dụng cặp ngoặc nhọn có các khoá và giá trị
Từ điển có thể thay đổi, thêm bớt....
"""

# Ví dụ 1
sinhVien = {
    "hoVaTen" : "Nguyen Van A",
    "maLop" : "ABC",
    "diemTrungBinh" : 8.5
}

print(sinhVien)

# In bằng khoá
print(sinhVien["hoVaTen"])

#In bằng get
print(sinhVien.get("maLop"))


# Thay đổi giá trị
sinhVien["maLop"] = "BCD"
print(sinhVien)

sinhVien.update({"maLop" : "ABE"})
print(sinhVien)


# Thêm key valua mới
sinhVien["namHoc"] = 2025
print(sinhVien)

sinhVien.update({"noiSinh" : "Hà Nội"})
print(sinhVien)


# Xoa di cac muc
sinhVien.pop("noiSinh")
print(sinhVien)

sinhVien.popitem() #Xoá cuối
print(sinhVien)

del sinhVien["hoVaTen"]
print(sinhVien)

# Xoá bỏ ra khỏi bộ nhớ del sinhVien

# Clear sạch bỏ key và valua
sinhVien.clear()
print(sinhVien)


sinhVien = {
    "hoVaTen" : "Nguyen Van A",
    "maLop" : "ABC",
    "diemTrungBinh" : 8.5
}

# Duyệt các giá trị
for x in sinhVien.values():
    print(x)

# Duyệt các cặp khoá
for x, y in sinhVien.items():
    print(x,y)

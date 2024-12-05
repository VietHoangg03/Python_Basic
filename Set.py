"""
Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trũ các tập
hợp dữ liệu, 3 kiểu còn lại là list [], tuple () và Dictionary {}, tất cả
đều có chất lượng và cách sử dụng khác nhau. 

Set là tập hợp không có thứ tự, không thể thay đổi và không được lập
chỉ mục. Lưu ý: các mục set là không thể thay đổi, nhưng bạn có thể
xoá các mục và thêm các mục mới

Sử dụng cặp ngoặc {}
"""
#Tạo ra một set mới
monHoc = {"Toán", "Lý", "Hoá"} 
print(monHoc)

#Duyệt phần tử
for x in monHoc:
    print(x)

#Thêm phần tử
monHoc.add("Lịch sử")
print(monHoc)
monHoc.add("Lịch sử") #Đè lên cái cũ ko trùng nhau
print(monHoc)

#Thêm nhiều phần tử
hocThem = {"Anh Văn", "Đàn"}
monHoc.update(hocThem)

# Thêm list vào SET
hocPhuDao = ["Võ thuật","Múa","Múa"]
print(hocPhuDao)
#Không thêm trùng được, duy nhất
monHoc.update(hocPhuDao)
print(monHoc)

# Xoá
monHoc.remove("Đàn")
print(monHoc)

# Discard xoá nếu có ko có thì bỏ qua
monHoc.discard("Đàn") #Không báo lỗi
print(monHoc)

# Xoá phần tử đầu tiên bằng pop
monHoc.pop()
print(monHoc)

# Xoá all
monHoc.clear()
print(monHoc)


# Xoá set
del monHoc
# Tạo list tỗng
emptyList = []

# Tạo ra một đối tượng List

emtryList2 = list()

print(emptyList)
print(emtryList2)


#Tạo ra list có dữ liệu
colors = ["red", "green", "orange"]
print(colors)

#Lít có thứ tự, vị trí 
studentList = ["An", "Bình", "Ngân", "Vy"]
print(studentList[2])
print(studentList[0])
print(studentList)
print(studentList[:])

# Xuất phát từ x đến y 
print(studentList[0:2])

# Thêm phần tử vào list
studentList.append("Thiên")
print(studentList)

studentList[len(studentList):] = ["Thành"]
print(studentList)

# Chèn vào vị trí x
studentList.insert(2, "Huy")
studentList.insert(2, "Huy")
studentList.insert(2, "Huy")
print(studentList)


# Số lương phần tử có trong list
print(len(studentList)) 

# Đếm số lượng phần tử thoả mãn điều kiện
print("Đếm Huy: ",studentList.count("Huy"))

# Xoá phần tử
studentList.remove("Ngân")
studentList.remove("Huy") #Xoá từ trái qua phải gặp nào đầu tiên xoá đó
print(studentList)

# Kiểm tra phần tử có bên trong list: in
if "Huy" in studentList:
    studentList.remove("Huy")
    print(studentList)



# Xoá phần tử ra khỏi list bằng vị trí
studentList.pop(2) 
print(studentList)

# Đảo ngược list
studentList.reverse()
print(studentList)


# Sắp xếp lại
studentList.sort()
print(studentList)

# Sắp xếp ngược
studentList.sort(reverse=True)
print(studentList)

# Xoá sạch dữ liệu trong list
studentList.clear()
print(studentList)
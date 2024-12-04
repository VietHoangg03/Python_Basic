a = 10
print(type(a))
b = 10.5
print(type(b))

c = True
print(type(c))

d = "Xin chào"
print(type(c))


s1 = "Xin chào"
s2 = "Hoàng"
s3 = s1 + s2
print(s3)

# Tạo chuỗi nhiều dòng
Chuoi_Nhieu_Dong = '''
Dòng 1
Dòng 2
Dòng 3
'''
print(Chuoi_Nhieu_Dong)


chep_phat = "Em hứa làm bài tập đầy đủ\n"
chep_phat_10 = chep_phat*10
print(chep_phat_10)


chuoi_1 = "Xin chào Hoàng"
chuoi_2 = "Hoàng"
chuoi_3 = "Việt Nam"

if chuoi_2 in chuoi_1:
    print("Chuỗi 2 là chuỗi con chuỗi 1")
else:
    print("Chuỗi 2 không là chuỗi con chuỗi 1")

if chuoi_3 in chuoi_1:
    print("Chuỗi 3 là chuỗi con chuỗi 1")
else:
    print("Chuỗi 3 không là chuỗi con chuỗi 1")

# Viết hoa chữ đầu chuỗi chuỗi
s = "hôm nay trời đẹp quá!"
s = str.capitalize(s)
print(s)


#Viết hoa toàn bộ chuỗi
s = s.upper()
print(s)

#Viết thường toàn bộ chuỗi
s = s.lower()
print(s)

# Đếm số lượng chuỗi con
s = "Lập trình Python là xu hướng hiện nay. Bạn nên học lập trình Python."
print(s.find("Python")) #Trả về -1 nếu ko tìm thấy

print(s.count("Python")) # Đếm số lượng


# Thay thế
s = s.replace("Python", "PYTHON")
print(s)


# Cắt chuỗi thành một LIST
list1 = s.split(" ")
print(list1)
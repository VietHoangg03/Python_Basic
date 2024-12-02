"""
Ép kiểu hay còn gọi là chuyển đổi kiểu dữ liệu
Quá trình chuyển đổi giá trị của một kiểu dữ liệu sang kiểu dữ liệu khác
gọi là ép kiểu.Python có hai kiểu chuyển đổi kiểu

Chuyển đổi ngầm định: Python tự chuyển đổi, ng dùng k tham gia
Chuyển đổi kiểu rõ ràng:
"""

a = 1
b = 2
c = a/b

print("Kiểu dữ liệu của a: ",type(a))
print("Kiểu dữ liệu của b: ",type(b))
print("Kiểu dữ liệu của c: ",type(c))

n = 100
m = "200"
#print(n+m) #Báo lỗi không cộng được với chuỗi
print(str(n) + m)
print(n + int(m))

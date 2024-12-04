# Vòng lặp đu từ 0 đến < n
n = 10
for i in range(n):
    print(i)

# Ví dụ tính tổng từ 0 -> n
n = input("Nhập vào n: ")
n = int(n)
tong = 0
for i in range(n + 1):
    tong += i
print(tong)

# Vòng lặp for, có bước tăng tuỳ chỉnh
for i  in range(0, 10, 2):
    print(i)

for i  in range(10, 0, -2):
    print(i)

# forr duyệt phần tử
colors = ["red","grenn","orange"]

for color in colors:
    print(color)

#Vòng lặp for duyệt phần tử theo vị trí
for i in range(len(colors)):
    print(colors[i])


# In bảng cửu chương
for i in range(11):
    print(" 2 X {0} = {1}".format(i, 2*i))


for j in range(2,10):
    print("Bảng cửu chương: ", j)
    for i in range(11):
        print(" {2} X {0} = {1}".format(i, j*i,j))
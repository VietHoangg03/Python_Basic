"""
Hàm là một khối mã chỉ chạy khi nó được gọi
Bạn có thể truyền dữ liệu, được gọi là tham số 
Kết quả là một hàm có thể trả về dữ liệu


Khai báo hàm:
def xinChao():
    print("Xin chào!")


Để gọi hàm: xinchao()
"""

# Tạo hàm xin chào
def xinChao():
    print("Xin chào!")

# Gọi hàm
xinChao()



# Tham số hay đối số (Agrumment)
def xinChao(hoVaTen):
    print("Xin chào: " + hoVaTen)
xinChao("Hoàng")



# Nhận nhiều đối số khác nhau, cách nhau bởi dấu phẩy
def xinChao(ho, chuLot, ten):
    print("Xin chào bạn: " + ho + chuLot + ten)
    print("Xin chào bạn: " + ho)

xinChao("Đinh", "Việt", "Hoàng")



# Khi không xác định được số đối số, chúng ta có thể sử dụng dấu *
def thoiKhoaBieu(*monHoc):
    print("Môn 1: " + monHoc[0])
    print("Môn 2: " + monHoc[1])

thoiKhoaBieu("Toán", "Lý", "Hoá")


def tinhTong(*giaTri):
    sum = 0
    for x in giaTri:
        sum = sum +x
    print(sum)

tinhTong(1, 3 ,4,6,7,8)


# Truyền nhiều đối số, xác định thông qua tên, sử dụng **
def xinChao(**hoVaTen):
    print("Xin chao: " + hoVaTen["ho"])

xinChao(ten = "Hoàng", chuLot = "Đinh", ho="Đinh")

# Sử dụng từ khoá "return" để trả về giá trị
def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich = tich*x
    return tich

tinh1 = tinhTich(1,2,3)
print(tinh1)


# Bài tập: Tìm USCLN của hai số a, b
# Xây dựng hàm: gcd(a,b) => Trả về USCLN
# Ví dụ: 1,13 => 1
# Ví dụ: 35,77 => 7
# Thuật toán đơn giản:
# 35, 42
# 35, 7
# 28, 7
# 21, 7
# 7, 7

def gcd(a, b):
    while(a!=b):
        if (a>b):
            a = a-b
        else:
            b = b- a
    return a

print(gcd(55,100))
print(gcd(11,121))


# Bài tập 2:
# Nhập vào một dãy (n) số từ bàn phím, sau đó tính tổng
# Yêu cầu:
# Xây dựng các hàm:
# nhap(n, list_number)
# tinhTong(list_number)


# Hàm nhập
list_number = []

n = -1
while(True):
    try:
        n = int(input("Nhập vào số lượng phần tử: "))
    except:
        print("Vui lòng nhập n> 1")
    if(n>1):
        break
def nhap(n, list_number):
    for i in range(n):
        list_number.append(int(input("Nhập vào giá trị thứ " + str(i)+": ")))

# Hàm tính tổng
def tinhTong(list_number):
    tong = 0
    for x in list_number:
        tong+=x
    return tong

nhap(n, list_number)
print("Tổng : "+str(tinhTong(list_number)))
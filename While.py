n = -1

while (n < 0):
    n =  int(input("Nhập vào n: "))


i = 0
tong = 0
while (i<=n):
    tong += i 
    i += 1
print("Tong = ", tong)


j = 0
while (j < 10):
    print(j, "Bên trong vòng lặp ")
    j+=1
else:
    print("Bên ngoài vòng lặp")
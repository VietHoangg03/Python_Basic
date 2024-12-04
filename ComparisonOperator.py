print("Ví dụ về toán tử so sánh: ")
x = int(input("x: "))
y = int(input("y: "))


# True hoặc flase
print("{0} < {1} là {2}".format(x,y,x<y))
print("{0} > {1} là {2}".format(x,y,x>y))
print("{0} == {1} là {2}".format(x,y,x==y))
print("{0} != {1} là {2}".format(x,y,x!=y))
print("{0} <= {1} là {2}".format(x,y,x<=y))
print("{0} >= {1} là {2}".format(x,y,x>=y))

print("Ví dụ về toán tử logic: ")
z= int(input("z: "))

print((x<y) and (y<z))
print((x>y) or (y>r))
print(not (x>z))

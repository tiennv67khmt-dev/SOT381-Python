# Giải phương trình bậc nhất 
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
if a == 0:
    if b != 0:
        print("Phương trình vô nghiệm.")
if a != 0:
    x = -b / a
    print(f"Phương trình có một nghiệm x = {x:.2f}")
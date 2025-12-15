a = int(input("Nhập một số nguyên N: "))
if a % 2 == 0:
    if a % 3 == 0:
        print(f"Số {a} là số chẵn và chia hết cho 3")
    else:
        print(f"Số {a} là số chẵn nhưng không chia hết cho 3")
else:
    print(f"Số {a} không phải là số chẵn")
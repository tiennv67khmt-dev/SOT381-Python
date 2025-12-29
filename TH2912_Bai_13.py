a = float(input("Nhập điểm Toán: "))
b = float(input("Nhập điểm Lý: "))
c = float(input("Nhập điểm Hóa: "))
Tong_diem = a + b + c 
if Tong_diem >= 15 and a >= 4 and b >= 4 and c >= 4:
    print("Đậu")
    if a > 5 and b > 5 and c > 5:
        print("Học đều các môn")
    else: 
        print("Học chưa đều các môn")
else:
    print("Thi hỏng")
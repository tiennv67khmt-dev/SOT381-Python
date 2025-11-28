print("=== TÍNH TIỀN ĐIỆN ===")

hoadon = float(input("Nhập số điện đã sử dụng: "))
if hoadon < 0:
    print("Số điện không hợp lệ!")
elif hoadon <= 50:
    tien = hoadon * 1.678
    print(f"Số tiền điện phải trả là: {tien:.3f} VNĐ")
elif hoadon <= 100:
    tien = 50 * 1.678 + (hoadon - 50) * 1.734
    print(f"Số tiền điện phải trả là: {tien:.3f} VNĐ")
elif hoadon <= 200:
    tien = 50 * 1.678 + 50 * 1.734 + (hoadon - 100) * 2.014
    print(f"Số tiền điện phải trả là: {tien:.3f} VNĐ")
elif hoadon <= 350:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + (hoadon - 200) * 2.536
    print(f"Số tiền điện phải trả là: {tien:.3f} VNĐ")
else:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 150 * 2.536 + (hoadon - 350) * 2.927
    print(f"Số tiền điện phải trả là: {tien:.3f} VNĐ")
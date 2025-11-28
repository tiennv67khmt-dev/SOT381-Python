print('=== TRÌNH QUẢN LÝ ĐIỂM HỌC SINH ===')

ten = input('Nhập tên học sinh: ')
toan = float(input('Nhập điểm Toán: '))
ly = float(input('Nhập điểm Lý: '))
hoa = float(input('Nhập điểm Hóa: '))
diem = (toan + ly + hoa) / 3
if diem >= 8:
    xeploai = 'Giỏi'
elif diem >= 6.5:
    xeploai = 'Khá'
elif diem >= 5:
    xeploai = 'Trung bình'
else:
    xeploai = 'Yếu'
print(f'''
Tên học sinh: {ten:>5}
Điểm trung bình: {diem:.2f}
Xếp loại: {xeploai:>5}
''')
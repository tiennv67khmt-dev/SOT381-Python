print('nhập điểm trung bình: ',end='')
diem = float(input())
if diem < 0 or diem > 10:
    print('Điểm không hợp lệ')
elif diem >=8:
    print('Giỏi')
elif diem >= 6.5 and diem <8:
    print('Khá')
elif diem >=5.0 and diem <6.5:
    print('Trung bình')
else:
    print('Yếu')
diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for diem in diem_so:
    if diem >=8:
        print(f'{diem}: học sinh giỏi')
    elif diem >= 6.5 and diem <= 7.9:
        print(f'{diem}: học sinh khá')
    else:
        print(f'{diem}: học sinh trung bình')
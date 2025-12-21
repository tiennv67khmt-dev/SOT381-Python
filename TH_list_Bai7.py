n = int(input('Nhập số môn học: '))
ds =[]
for i in range(n):
    diem = float(input(f'Nhập điểm môn thứ {i+1}: '))
    ds.append(diem)
diem_tb = sum(ds) / n 
print(f'Điểm trung bình là: {diem_tb:.2f}')
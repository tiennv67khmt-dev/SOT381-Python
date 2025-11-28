print('=== Chuyển đổi nhiệt độ ===')
nhietdo = float(input('Nhập nhiệt độ: '))
loai = input('Nhập loại (C/F/K): ' ).upper()
if loai == 'C':
    F = nhietdo * 1.8+32
    K = nhietdo +273.15
    print(f'Nhiệt độ tương đương: {F:.2f}°F, {K:.2f}K')
elif loai == 'F':
    C = (nhietdo -32)/1.8
    K = (nhietdo -32)/1.8 +273.15
    print(f'Nhiệt độ tương đương: {C:.2f}°C, {K:.2f}K')
elif loai == 'K':
    C = nhietdo -273.15
    F = (nhietdo -273.15) * 1.8 +32
    print(f'Nhiệt độ tương đương: {C:.2f}°C, {F:.2f}°F')
else:
    print('Loại nhiệt độ không hợp lệ! Vui lòng nhập C, F hoặc K.')
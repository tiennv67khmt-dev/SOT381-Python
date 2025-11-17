print('Nhập tuổi của bạn:', end="")
tuoi = int(input())
if tuoi < 0:
    print('Tuổi không hợp lệ.')
elif tuoi < 18:
    print('Bạn chưa đủ tuổi bầu cử.')
else:
    print('Bạn đủ tuổi bầu cử.')
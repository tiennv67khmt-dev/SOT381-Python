print('nhập năm: ',end="")
nam = int(input())
if (nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0):
    print('Năm nhuận')
else:
    print('Năm không nhuận')
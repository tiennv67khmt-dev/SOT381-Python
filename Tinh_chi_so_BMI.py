print('nhâp cân nặng (kg):', end="")
can_nang = float(input())
print('nhập chiều cao (m):', end="")
chieu_cao = float(input())
bmi = can_nang / (chieu_cao ** 2)
print('Chỉ số BMI của bạn là:', bmi)
if bmi < 18.5:
    print('Bạn bị thiếu cân.')
elif 18.5 <= bmi < 24.9:
    print('Bạn có cân nặng bình thường.')
elif 25 <= bmi < 29.9:
    print('Bạn bị thừa cân.')
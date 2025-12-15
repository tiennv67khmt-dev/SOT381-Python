n = input("Nhập: ")
while n != 'y' and n != 'Y':
    n = input("Nhập lại: ")
while n == 'y' or n == 'Y':
    print("Login success")
    break
print('username: ',end='')
u = str(input())
print('password: ',end='')
p = int(input())
if u == 'admin' and p == 123456:
    print('Đăng nhập thành công')
else:
    print('Đăng nhập thất bại')
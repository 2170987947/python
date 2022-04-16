# 姓名：fmm
# 开发时间：2022/4/16 17:50
a = 0
while a < 3:
    pwd = input('请输入密码：')
    if pwd == '123':
        print('密码正确')
        break
    else:
        print('密码错误')
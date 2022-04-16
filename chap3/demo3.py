# 姓名：fmm
# 开发时间：2022/4/16 16:04
a = int(input('请输入一个分数：'))
if a > 100 or a < 0:
    print('输入错误')
    exit(0)
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
elif a >= 0:
    print('E')
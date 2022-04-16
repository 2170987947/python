# 姓名：fmm
# 开发时间：2022/4/16 17:32
for a in range(100, 1000):
    ge = a % 10
    shi = a // 10 % 10
    bai = a // 100 % 10
    if ge**3 + shi**3 + bai**3 == a:
        print(a)

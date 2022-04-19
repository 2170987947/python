# 姓名：fmm
# 开发时间：2022/4/20 1:32
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)
print(fac(6))

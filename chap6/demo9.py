# 姓名：fmm
# 开发时间：2022/4/20 1:35
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(6))

for i in range(1, 7):
    print(fib(i))
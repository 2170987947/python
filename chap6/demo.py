# 姓名：fmm
# 开发时间：2022/4/20 0:05
def fun(n1, n2):
    print('n1 = ', n1)
    print('n2 = ', n2)
    n1 = 100
    n2.append(10)
    print('n1 = ', n1)
    print('n2 = ', n2)

n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print(n1)
print(n2)
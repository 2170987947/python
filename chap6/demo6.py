# 姓名：fmm
# 开发时间：2022/4/20 1:00
def fun(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

fun(1, 2, 3, 4)
fun(a=11, b =22, c=33, d=44)
fun(111, 222, c=333, d=444)

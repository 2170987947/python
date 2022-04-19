# 姓名：fmm
# 开发时间：2022/4/20 1:00
def fun(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

fun(111, 222, c=333, d=444)

def fun1(a, *, b, **args):
    pass
def fun2(a,  b, *args, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)
fun2(1, 2, 3, 4, m=5, n=6)
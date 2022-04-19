# 姓名：fmm
# 开发时间：2022/4/20 0:31
def fun(*args):
    print(args)

fun(10)
fun(10, 20)
fun(10, 20, 30)

def fun2(**args):
    print(args)

fun2(a=10)
fun2(a=20, b=30)
fun2(a=40, b = 50, c = 60)

def fun3(*args1, **args2):
    print(args1)
    print(args2)

fun3(1, 2, a = 3, b = 4, c = 5)
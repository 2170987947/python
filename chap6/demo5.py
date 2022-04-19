# 姓名：fmm
# 开发时间：2022/4/20 0:43
def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)

fun(10, 20, 30)
lst = [11, 22, 33]
fun(*lst)
fun(a=100, b =200, c=300)
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)
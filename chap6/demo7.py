# 姓名：fmm
# 开发时间：2022/4/20 1:23
def fun1(a, b):
    c = a + b
    print(c)
fun1(1, 2)

name = 'fmm'
def fun2():
    print(name)
fun2()

def fun3():
    global age
    age = 10
    print(age)
fun3()
print(age)

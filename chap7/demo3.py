# 姓名：fmm
# 开发时间：2022/4/20 9:00
a = 20
b = 100
c = a + b
d = a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name

stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2
print(s)

lst = ['ed', 'po', 'dd']
print(lst.__len__())
print(len(lst))
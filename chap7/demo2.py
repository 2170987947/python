# 姓名：fmm
# 开发时间：2022/4/20 8:32
class Person:
    pass
class Student(Person, object):
    name = 'fmm'
    def __init__(self, age):
        self.age = age
    def study(self):
        print('实例方法：', self.name)
stu1 = Student(10)
print(type(stu1))
print(stu1.__dict__)
print(Student.__dict__)
print(stu1.__class__)
print(Student.__bases__)
print(Student.__base__)
print(Student.__mro__)
print(Person.__subclasses__())

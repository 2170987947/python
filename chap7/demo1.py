# 姓名：fmm
# 开发时间：2022/4/20 2:13
class Student:
    native_place = '陕西'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('我的名字叫：', self.name, '年龄是：', self.age)

    @classmethod
    def cm(cls):
        print('类方法')

    @staticmethod
    def sm():
        print('静态方法')

stu1 = Student('张三', 20)
stu1.info()
Student.info(stu1)
stu1.cm()

print(id(stu1))
print(type(stu1))
print(stu1)

print(id(Student))
print(type(Student))
print(Student)
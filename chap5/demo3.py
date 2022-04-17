# 姓名：fmm
# 开发时间：2022/4/18 0:48
s = 'Python'
print(s, id(s))
a = s.upper()
print(a, id(a))
b = s.lower()
print(b, id(b))
c = b.lower()
print(c, id(c))

s2 = 'Hello World!'
print(s2.swapcase())

s3 = 'pcnD DfGY dFds'
print(s3.capitalize())
print(s3.title())

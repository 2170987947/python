# 姓名：fmm
# 开发时间：2022/4/17 14:29
a = ('Python', 98, 'world')
print(id(a), type(a), a)

b = tuple(('Python', 99, 'World'))
print(id(b), type(b), b)

t = tuple((0,))
print(id(t), type(t), t)

t = (0,)
print(id(t), type(t), t)

# d = {}
d = dict()
f = list()
print(d)
print(f)

tt = ()
tt2 = tuple()

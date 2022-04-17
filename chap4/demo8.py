# 姓名：fmm
# 开发时间：2022/4/17 14:26
lst = [10, 20, 30]
print(id(lst))
lst.append(40)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
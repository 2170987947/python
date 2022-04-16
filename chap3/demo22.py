# 姓名：fmm
# 开发时间：2022/4/17 0:00
lst = ['hello', 98, 'world', 'rfc', 99, 98]
lst.remove(98)
print(lst)

lst.pop(1)
print(lst)

# print(lst[1:3])
lst[1:3] = []
print(lst)

lst.clear()
print(lst)

del lst
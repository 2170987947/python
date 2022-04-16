# 姓名：fmm
# 开发时间：2022/4/17 0:18
lst = [10, 0, 90, 60, 70]
print(lst, id(lst))
lst.sort()
print(lst, id(lst))
lst.sort(reverse=True)
print(lst, id(lst))

lst = [10, 0, 90, 60, 70]
print(lst)
lst2 = sorted(lst)
print(lst2)
lst2 = sorted(lst, reverse=True)
print(lst2)
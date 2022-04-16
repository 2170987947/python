# 姓名：fmm
# 开发时间：2022/4/16 23:46
lst = ['hello', 98, 'world']
lst.append('hjk')
print(lst)

lst2 = ['hh', 90, 'hd']
lst.append(lst2)
print(lst)
lst.extend(lst2)

print(lst)
lst.insert(1, lst2)
print(lst)

lst[1:1] = lst2
print(lst)
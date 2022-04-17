# 姓名：fmm
# 开发时间：2022/4/17 17:02
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print((s1 - s2) | (s2 - s1))

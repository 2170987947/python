# 姓名：fmm
# 开发时间：2022/4/17 16:56
s1 = {10, 20, 30, 40}
s2 = {40, 30, 20, 10}
print(s1 == s2)
s3 = {10, 20, 30}
s4 = {10, 20, 90}
print(s3.issubset(s2))
print(s4.issubset(s2))
print(s2.issuperset(s3))
print(s2.issuperset(s4))
print(s3.isdisjoint(s4))

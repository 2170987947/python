# 姓名：fmm
# 开发时间：2022/4/17 12:25
scores = {'张三': 100, '李四': 60, '王五': 20}
print(id(scores), type(scores))
print(scores)

scores2 = dict({'张三': 100, '李四': 60, '王五': 20})
print(id(scores2), type(scores2))
print(scores2)

scores3 = dict(张三=100, 李四=60, 王五=20)
print(id(scores3), type(scores3))
print(scores3)

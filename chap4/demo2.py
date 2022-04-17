# 姓名：fmm
# 开发时间：2022/4/17 12:44
scores = {'张三': 100, '李四': 60, '王五': 20}
print(scores['李四'])
print(scores.get('王五'))
print(scores.get('lll'))
# print(scores['lll'])
print(scores.get('lll', 99))
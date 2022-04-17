# 姓名：fmm
# 开发时间：2022/4/17 13:04
scores = {'张三': 100, '李四': 60, '王五': 20}
print('张三' in scores)
print('张' not in scores)
del scores['张三']
print(scores)
scores['lll'] = 67
print(scores)
scores['lll'] = 100
print(scores)
scores.clear()
print(scores)
del scores


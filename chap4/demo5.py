# 姓名：fmm
# 开发时间：2022/4/17 13:27
scores = {'张三': 89, '李四': 59, '王五': 20, '小六': 99}
for item in scores:
    print(item, scores[item], scores.get(item))
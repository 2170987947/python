# 姓名：fmm
# 开发时间：2022/4/17 13:44
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 100]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
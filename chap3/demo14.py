# 姓名：fmm
# 开发时间：2022/4/16 17:52
for item in range(1, 51):
    if (item % 5 == 0):
        print(item)

for item in range(1, 51):
    if (item % 5 != 0):
        continue
    print(item)
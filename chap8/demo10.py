# 姓名：fmm
# 开发时间：2022/4/22 13:57
import os
for i in os.listdir(os.getcwd()):
    if i.endswith('.py'):
        print(i)
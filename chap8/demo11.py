# 姓名：fmm
# 开发时间：2022/4/22 14:01
import os
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print(dirpath)
    print(dirname)
    print(filename)
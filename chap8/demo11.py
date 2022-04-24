# 姓名：fmm
# 开发时间：2022/4/22 14:01
import os
for dirpath, dirname, filename in os.walk(os.getcwd()):
    # print(dirpath)
    # print(dirname)
    # print(filename)
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in filename:
        print(os.path.join(dirpath, file))
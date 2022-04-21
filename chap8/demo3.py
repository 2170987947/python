# 姓名：fmm
# 开发时间：2022/4/21 23:33
file = open('CET-4.jpg', 'rb', encoding="utf-8")
target_file = open('CET-41.jpg', 'wb', encoding="utf-8")
target_file.write(file)
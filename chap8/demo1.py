# 姓名：fmm
# 开发时间：2022/4/20 11:50
file = open('a.txt', 'r', encoding='UTF-8')
target_file = open('c.txt', 'w', encoding='utf-8')
target_file.write(file.read())
file.close()
target_file.close()

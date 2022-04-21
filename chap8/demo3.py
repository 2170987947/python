# 姓名：fmm
# 开发时间：2022/4/21 23:33
file = open('CET-4.jpg', 'rb')
target_file = open('CET-41.jpg', 'wb')
target_file.write(file.read())
file.close()
target_file.close()
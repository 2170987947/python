# 姓名：fmm
# 开发时间：2022/4/22 13:05
with open('CET-4.jpg', 'rb') as src_file:
    with open('copyCET-4.jpg', 'wb') as target_file:
        target_file.write(src_file.read())
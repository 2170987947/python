# 姓名：fmm
# 开发时间：2022/4/22 13:38
import os.path
print(os.path.abspath('demo9.py'))
print(os.path.exists('demo9.py'))
print('   ', os.path.join('D:\\Git\\python\\python\\chap8', 'demo9.py'))
print(os.path.splitext('D:\\Git\\python\\python\\chap8.py'))
print(os.path.dirname('D:\\Git\\python\\python\\chap8.py'))
print(os.path.isdir('D:\\Git\\python\\python\\chap8.py'))
print(os.path.isdir('D:\\Git\\python\\python'))
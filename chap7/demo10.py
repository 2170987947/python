# 姓名：fmm
# 开发时间：2022/4/20 11:11
import sys
import time
import urllib.request
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())
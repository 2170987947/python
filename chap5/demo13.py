# 姓名：fmm
# 开发时间：2022/4/19 0:07
s = '窗前明月光'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))

byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte2 = s.encode(encoding='UTF-8')
print(byte2.decode(encoding='UTF-8'))
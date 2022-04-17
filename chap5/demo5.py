# 姓名：fmm
# 开发时间：2022/4/18 1:14
s = 'hello world Python'
print(s.split())
s2 = 'hello|world|Python'
print(s2.split(sep="|"))
print(s2.split(sep="|", maxsplit=1))

s = 'hello world Python'
print(s.rsplit())
s2 = 'hello|world|Python'
print(s2.rsplit(sep="|"))
print(s2.rsplit(sep="|", maxsplit=1))
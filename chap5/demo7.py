# 姓名：fmm
# 开发时间：2022/4/18 15:45
s = 'hello, python'
print(s.replace('python', 'Java'))
s2 = 'hello, python, python, python'
print(s2.replace('python', 'Java', 2))

lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

lst2 = ['hello', 'java', 'Python']
print('|'.join(lst2))
print('*'.join(lst2))

print('|'.join('Python'))

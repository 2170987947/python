# 可以输出数字
print(98.5);
print('Hello World');
print("Hello World");

print(3 + 1);
print('3 + 1');

# 将数据输出文件中，注意点：
#所在盘符是否存在
#使用file=fp
fp = open('F:/text.txt', 'a+');
print('Hello World', file = fp);
fp.close();

print('hello', 'world', 'Python');

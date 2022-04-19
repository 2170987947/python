# 姓名：fmm
# 开发时间：2022/4/20 0:14
print(bool(0))
print(bool(-1))

def fun(nums):
    odd = []
    even = []
    for i in nums:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

lst = [10, 29, 34, 34, 23, 45, 80]
print(fun(lst))
# 姓名：fmm
# 开发时间：2022/4/22 12:56

class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
    def show(self):
        print('show方法被调用执行了')
with MyContentMgr() as file:
    file.show()
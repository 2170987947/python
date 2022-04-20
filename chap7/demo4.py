# 姓名：fmm
# 开发时间：2022/4/20 9:26
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()
cpu2 = cpu1
print(id(cpu1), id(cpu2))

disk = Disk()
computer = Computer(cpu1, disk)
import copy
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)

def fun1():
    print('我是个函数')
computer3.f = fun1
computer3.f()


# 姓名：fmm
# 开发时间：2022/4/24 9:16

def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():
    pass

def search():
    pass

def delete():
    pass

def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

def menu():
    print('=======================学生信息管理系统=======================')
    print('---------------------------功能菜单--------------------------')
    print('            1.录入学生信息')
    print('            2.查找学生信息')
    print('            3.删除学生信息')
    print('            4.修改学生信息')
    print('            5.排序')
    print('            6.统计学生总人数')
    print('            7.显示所有学生信息')
    print('            0.退出系统')
    print('-------------------------------------------------------------')

if __name__ == '__main__':
    main()

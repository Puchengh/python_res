


def func():
    print('-----循环导入2里面的func1-----')
    from study.包.循环导入1 import task1
    task1()
    print('-----循环导入2里面的func2-----')

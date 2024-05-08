def task1():
    print('-----task1-----')

def task2():
    from study.包.循环导入2 import func
    func()
    print('-----task2-----')

if __name__ == '__main__':
    task1()
    task2()


"""
在加载的过程中也会执行不在mian里面的函数
if __name__ == '__main__':
    task1()
    task2()
结果：
    -----task1-----
    -----循环导入2里面的func1-----
    -----task1-----
    -----循环导入2里面的func2-----
    -----task2-----
    
task1()
task2()

结果:
    -----task1-----
    -----循环导入2里面的func1-----
    -----task1-----
    -----循环导入2里面的func1-----
    -----task1-----
    -----循环导入2里面的func2-----
    -----task2-----
    -----task1-----
    -----循环导入2里面的func2-----
    -----task2-----
"""
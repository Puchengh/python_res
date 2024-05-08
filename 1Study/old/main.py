# 这是一个示例 Python 脚本。

from __future__ import print_function

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本
if __name__ == '__main__':
    print_hi('PyCharm')
    # print_ni('ni')


# 哈希是一种算法，其中做的就是提取数据的特征码

# 在python中 是不允许直接修改全局变量的值，先找局部变量   如果没有就会去找全局变量  如果需要修改全局变量  则需要使用global关键字
# 全局变量前面加g_或者gl_
# 返回多个值是返回一个元组,需要单独拿出来，如果返回的是元组，可以定义多个变量记录
# a,b = (b,a)  python专有 --也可以省略小括号 a, b = b, a

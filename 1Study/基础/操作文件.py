'''
写文件
从开始写到close()属于一次
只要mode是  'w'模式，表示的就是写操作
方法:
    write(内容)  每次都会将原来的内容清空,然后写当前的内容 (覆盖)
    writelines（iterable）  没有换行的效果      writelines（iterable）  没有换行的效果  stream.writelines(['赌神高进\n','赌侠周星星\n','赌圣小刀\n'])

如果 mode = 'a'  表示的追加  就不会清空原来的的内容  append

'''

# stream = open(r'D:\chenpu\tmp\aaa.txt', 'a')
# # reluse  = stream.writable()  #是否有写的权限
# # print(reluse)  #结果是True  boolean类型
#
# # s = '''
# # 你好
# #     欢迎!a
# #         高进
# # '''
#
# result = stream.write('hello')  #覆盖原文件
# print(result)
#
# stream.write('龙五\n')
#
# stream.writelines(['赌神高进\n','赌侠周星星\n','赌圣小刀\n'])
#
#
# stream.write('僵尸先生')
# stream.close()


'''
文件的复制：
read mode = 'rb'
write mode = 'wb'
with 结合open使用  可以自动释放资源

'''
# stream = open(r'D:\chenpu\tmp\p1\girl.jpg', 'rb')
# with open(r'D:\chenpu\tmp\p1\girl.jpg', 'rb') as stream:
#     container = stream.read()   #读取文件内容
#     print(stream.name)
#     file = stream.name
#     fielname = file[file.rfind('\\')+1:]
#     print(fielname)
#
#     with open(r'D:\chenpu\tmp\p2\girl.jpg', 'wb') as wstream:
#         wstream.write(container)
#
# print('文件复制完成!')


'''
operating system   xxx.py
os.path.dirname(__file__)  获取当前文件所在的文件目录（绝对路径）

'''
# import os
# import functools
#
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
# result = os.path.join(path, 'girl.jpg')
# print(path)
# print(result)
# print(type(result))
#
# # os.path.abspath()  #判断是不是绝对路径
# os.path.isabs('tmp/p2/girl.jpg')  # 判断是不是绝对路径
# os.path.isabs('../tmp/p2/girl.jpg')  # 上一级的目录下面的文件

# path =os.path.dirname(__file__)
# print(path)


# 通过相对路径得到绝对路径

# path = os.path.abspath('test.py')
# print(path)

# path = os.path.abspath(__file__)
# print(path)


# 可以得到当前目录
# path = os.getcwd()
# print(path)
#
# path = r'C:\Users\v_wbpuchen\PycharmProjects\test\操作文件.py'
# result = os.path.split(path)  #可以拿到文件名  保存在元组中
#
# print(result)
#
# # fielname = path[path.rfind('\\')+1:]
# filename = result[1]   #可以拿到文件名
# print(result[1])
#
#
# result = os.path.splitext(path)  #分割文件和扩展名  ('C:\\Users\\v_wbpuchen\\PycharmProjects\\test\\操作文件', '.py')
# print(result)
#
# size = os.path.getsize(path)   #返回有个文件的大小  单位是字节
# print(size)


'''
dirname()
join ()   连接路径
split() 
splitext()
getsize()

isabs() 是不是绝对路径
isfile()   是不是一个文件
isir()  是不是一个文件夹
'''

# result = os.path.join(os.getcwd(),'file','a','a1.jpg')
# print(result)


'''
os模块下面的方法:
os.getcwd()  获取当前路径
os.listdir()   浏览文件夹
os.mkdir()   创建文件夹
os.rmdir()  删除空的文件加
os.remove()  删除我呢缉拿
os.chdir()   切换目录
'''

import os
# dir = os.getcwd()
# print(dir)
#
#
# all = os.listdir(r'D:\chenpu\tmp\p1')  # 返回指定目录下的所有文件和文件夹 保存在列表中
# print(all)
#
#
# #创建文件夹
# if not os.path.exists(r'D:\chenpu\tmp\p3'):
#     os.mkdir(r'D:\chenpu\tmp\p3')  # 创建文件夹
#
# # os.rmdir(r'D:\chenpu\tmp\p3')  #目录不是空的  只能移除空文件夹
#
# # os.removedirs(r'D:\chenpu\tmp\p3')  #删除多个目录  只要里面有东西就不能删除
#
# os.remove(r'D:\chenpu\tmp\p3\p4\aaa.txt')

# 删除p4这个文件夹
# path  = r'D:\chenpu\tmp\p3\p4'
# filelist  = os.listdir(path)
# for file in filelist:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
#     print('删除成功!')


# path = os.getcwd()
# print(path)
# # 切换目录
# os.chdir(r'D:\chenpu\tmp\p3')  #返回值为none  切换文件夹的目录
# path = os.getcwd()
# print(path)


import os

# 文件夹复制
src_path = r'D:\chenpu\tmp\p1'
target_path = r'D:\chenpu\tmp\p2'


# # 封装成函数
# def copy(src_path, target_path):
#     if os.path.isdir(src_path) and os.path.isdir(target_path):  # 判断是不是文件夹
#         files = os.listdir(src_path)  # ['aaa.txt','']
#         for file in files:
#             path = os.path.join(src_path, file)
#             with open(path, 'rb') as stream:
#                 container = stream.read()
#                 path1 = os.path.join(target_path, file)
#                 with open(path1, 'wb') as stream:
#                     stream.write(container)
#         else:
#             print('复制完毕！')
#
# # 调用当前函数
# copy(src_path, target_path)


# def copy(src_path,target_path):
#     files = os.listdir(src_path)  #获取文件夹里面的内容
#     print(files)
#     #变量列表
#     for file in files:
#         #拼接路径
#         path  = os.path.join(src_path,file)
#         if os.path.isdir(path):
#             #在目标文件里面创建对应的源文件同名的文件夹
#             path2  = os.path.join(target_path,file)
#             os.mkdir(path2)
#             #递归调用copy
#             copy(path,path2)
#         else:
#
#             with open(path, 'rb') as stream:
#                 container = stream.read()
#                 path1 = os.path.join(target_path, file)
#                 with open(path1, 'wb') as stream:
#                     stream.write(container)
#
#     else:
#         print('复制完成')
#
# copy(src_path,target_path)


'''
文件上传:  E:\py\test.py | E:\py\aaa.txt  | E:\py\1.jpg

mode r w   纯文本文件
     rb :binary  读二进制  图片 音乐 影片
     wb
open(file，mode,buffering, endcoding)

open(path/filename,rt)  默认是rt  t是text格式

stream.read() 读取管道里面的内容
不能同时读取  如果上面对一个文件进行读取  下面的读不到这个文件的

如果是图片不能使用默认的读取方式  应该使用rb二进制的形势
'''

# stream = open(r'E:\py\aaa.txt',mode='rt')
# conteriner = stream.read()
# print(conteriner)
# # conteriner = stream.readable()   #打印出来文件是不是有可读权限  True或者False
# conteriner1 = stream.readline()
# print(conteriner1)
# # print(stream.encoding)  #打印编码

# while True:
#     line = stream.readline()   #默认加一个空行
#     print(line)
#     if not line:
#         break

# lines = stream.readlines()  #保存在列表中  ['hello word\n', '11111']
#
#
# for i in lines:
#     print(i)
# print(lines)

stream = open(r'E:\py\1.jpg',mode='rb')
conteriner = stream.read()
print(stream)
print(conteriner)

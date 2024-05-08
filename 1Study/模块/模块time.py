"""
time模块
"""
# import time
# # 返回时间戳
# # t = time.time()   #1699777419.4627287
# # time.sleep(1)
# # t1 = time.time()
# # print(t)
# # print(t1)
#
# # 转换成字符串
# # s = time.ctime(1)  #def ctime(seconds=None)
# # print(s)
#
# # 时间转换成元组
# s = time.localtime()
# print(s)
# print(s.tm_year)
# print(s.tm_hour)
#
# #####################前面三个可以不带参数#####################
#
# # 将元组转成时间戳
# tt = time.mktime(s)  #必须带参数
# print(tt)
#
# """
#     %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
# """
# # 将元组转成字符串
# ttt = time.strftime('%Y-%m-%d %H:%M:%S')
# print(ttt)
#
# #将字符串转成元组的方式
# strp = time.strptime('20231001','%Y%m%d')
# print(strp)


import datetime
import time

print(datetime.time.hour)   #得到的是一个对象
print(time.localtime().tm_hour)  #16

print(time.time())   #1699778491.3179805


d = datetime.date(2023, 11, 12)
print(datetime.date.ctime(d))  # Sun Nov 12 00:00:00 2023

print(datetime.date.today())   # 2023-11-12

# timedel = datetime.timedelta(days=2,hours=10)
timedel = datetime.timedelta(days=2)
print(timedel)

now = datetime.datetime.now()
print(now)   # 2023-11-12 16:45:55.482904
result = now - timedel
print(result)    # 2023-11-10 16:45:55.482904



# 缓存 数据redis 作为缓存 redis.set(key,value,保存时间)  sessin缓存


import random

# 生成四位的验证码
# stringg = 'abcdefhigklmnopqrstuvwxyzABCDEFHIGKLMNOPQRSTUVWXYZ1234567890'  #如果是固定的常量  是会放在import之后
# filename = ''
# for i in range(4):
#     index = random.randint(0, len(stringg) - 1)
#     filename += stringg[index]
# print(filename)
'''
只有range是左闭右闭  其他都是左闭右开
'''

# s = 'A1234'
# result = s.isalpha()  # 是否全都是字母组成
# print(result)
#
# s1 = '1234'
# result1 = s1.isdigit()  # 是否全都是数字组成
# print(result1)
#
#
# s1 = '1234'
# result = s1.isalnum() # 是否由数字或者字母组成
# print(result)
#
#
# s = '  '
# result = s.isspace()   # 字符串里面是有空格
# print(result)
#
#
# s = 'hellO'
# result = s.isupper()   # 字符串里面是不是全都是大写
# print(result)
#
# s = 'hell1'
# result = s.islower()    # 字符串里面是不是全都是小写
# print(result)

'''
用户名或者手机号登录+密码
用户名:全部小写，首字母不能是数字，长度必须6位以上
手机号:纯数字，长度是11位
密码必须是6位数字

以上符合条件则进入下层验证:
判断用户名:密码  是否是正确的 则成功  否则失败
'''

while True:
    name = input('用户名/手机号',)
    # 判断
    if name.islower() and len(name) >= 6 and not name[0].isdigit():
        # 输入密码
        while True:
            password = input('输入密码:')
            if password.isdigit() and len(password) == 6:
                print('登录成功!')
                break
            else:
                print('密码必须是六位数字!')
    else:
        print('用户名或者手机号格式错误')



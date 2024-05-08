'''
装饰器 会和web开发的时候使用
带返回值的装饰器  有返回值的函数
相当于是java中的重写
原函数中有返回值，装饰器的内部函数也要有返回值
'''

# def decorater(func):
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs)
#         print('预计装修{}元'.format(r))
#         print('刷漆')
#         return 60000
#     return wrapper
#
# @decorater
# def house():
#     print('i am a house....')
#     return 50000
#
# r = house()   #house就是wrapper
# print(r)


def outer_check(time):
    print('-------1')
    def check_time(action):
        print('-------3')
        def do_action():
            if time < 22:
                return action()
            else:
                return '对不起,您不具有该权限'
        print('-------4')
        return do_action

    print('-------2')
    return check_time

@outer_check(23)
def paly_game():
    #调了两次   outer_check(23)  r=check_time --> check_time(play_game)
             # --> paly_game = doaction
    return '玩游戏'

# print(paly_game())
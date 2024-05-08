# 停车计费系统

# 没有车辆
car_park = []


def enter():
    print('欢迎进入停车场！')
    number = input('输入车牌号码:')

    car = {}
    car[number] = [0]

    car_park.append(car)


def go_out():
    number = input('输入车牌号:')
    for car in car_park:
        if number in car:
            pass
    else:
        print('此车未进场')

# 支持服务访问
# web框架
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

heros = ['黑暗之女', '狂战士', '正义巨像', '卡牌大师', '德邦总管', '无畏战车', '诡术妖姬', '猩红收割者', '远古恐惧',
         '正义天使', '无极剑圣', '牛头酋长', '符文法师', '亡灵战神', '战争女神', '众星之子', '迅捷斥候', '麦林炮手',
         '祖安怒兽', '雪原双子', '赏金猎人', '寒冰射手', '蛮族之王', '武器大师', '堕落天使', '时光守护者', '炼金术士',
         '痛苦之拥', '瘟疫之源', '死亡颂唱者', '虚空恐惧', '殇之木乃伊', '披甲龙龟', '冰晶凤凰', '恶魔小丑', '祖安狂人',
         '琴瑟仙女', '虚空行者', '刀锋舞者', '风暴之怒', '海洋之灾', '英勇投弹手', '天启者', '瓦洛兰之盾', '邪恶小法师',
         '巨魔之王', '诺克萨斯统领', '皮城女警', '蒸汽机器人', '熔岩巨兽', '不祥之刃', '永恒梦魇']


@app.route('/index')
def index():
    return render_template('index.html', heross=heros)


@app.route('/lottery')
def lottery():
    num = randint(0, len(heros) - 1)
    return render_template('index.html', heross=heros, h=heros[num])


app.run(debug=True)

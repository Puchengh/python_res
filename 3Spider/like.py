# 支持服务访问
# web框架
from flask import Flask, render_template,request
from random import randint

app = Flask(__name__)

data = [{'id': 0, 'name': '中秋节', 'num': 0},
        {'id': 1, 'name': '春节', 'num': 0},
        {'id': 2, 'name': '建军节', 'num': 0},
        {'id': 3, 'name': '国庆节', 'num': 0}
        ]


@app.route('/index')
def index():
    return render_template('index_like.html',data =data)

@app.route('/dainzan')
def dainzan():
    id = request.args.get('id')
    print(f'想要给{id}点赞!')

    data[int(id)]['num'] += 1
    return render_template('index_like.html',data =data)

app.run(debug=True)

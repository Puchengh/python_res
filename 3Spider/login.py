from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    username = request.args.get('username')
    return '欢迎登录:{}'.format(username)

app.run(debug=True)
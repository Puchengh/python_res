# 发送请求
import requests
from lxml import etree
from flask import Flask, render_template,request

app = Flask(__name__)  #创建一个web应用
def get_phone(phone):
    # 发送地址
    url = f'https://m.ip138.com/sj.asp?mobile={phone}'

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    req = requests.get(url,headers=headers)
    req.encoding = 'utf-8'

    e = etree.HTML(req.text)

    datas = e.xpath('//tr/td/a[1]/text()')
    print(datas)

    return datas

# get_phone(16611018888)

@app.route('/')
def index():
    return render_template("templates/phone.html")

@app.route('/search_phone')
def search_phone():
    phone = request.args.get('phone')
    data = get_phone(phone)
    return '<br/>'.join(data)

app.run(debug=True)
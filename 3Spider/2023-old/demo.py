# import requests
#
# # 模拟一个构造headers请求头信息
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }
# # 发送请求
# r = requests.get('https://www.douban.com', headers=headers)
# # r = requests.request('get', 'https://www.douban.com')
# print(r.headers)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# import requests
#
# # 构建参数的字典
# kw = {
#     'wd': 'python'
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }
# response = requests.get('http://www.baidu.com/s?', params=kw, headers=headers)
# response.encoding = 'utf-8'
# print(response.text)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import requests

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'

data = {
    'log': 'puchen',
    'pwd': '*z(CH*%%aRr!Dj2Q',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

respone = requests.post(url, data=data, headers=headers)
respone.encoding = 'utf-8'
print(respone.text)

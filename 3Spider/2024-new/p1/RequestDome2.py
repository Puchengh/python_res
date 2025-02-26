import requests

url = 'https://fanyi.baidu.com/sug'
str = input("请输入你要翻译的单词:")

dat = {
    "kw": str
}

resp = requests.post(url,data=dat)

print(resp.json())  #将服务器返回的结果直接处理成json => dict


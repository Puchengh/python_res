import requests

query = input("输入一个你喜欢的明星:")

url = f'https://www.sogou.com/web?query={query}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
resp = requests.get(url, headers=headers)  # 处理反爬

print(resp)
print(resp.text)

import requests
from lxml import etree

url = 'https://dl.131437.xyz/book/douluodalu1/2.html'

while True:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # 发送请求
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    # 响应请求
    # print(resp.text)


    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    url = f'https://dl.131437.xyz{e.xpath("//tr/td[2]/a/@href")[0]}'
    # print(info)
    print(title)

    with open('./novel/斗罗大陆.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')

    #退出循环
    if url == 'https://dl.131437.xyz/book/douluodalu1/5.html':
        break
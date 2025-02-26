# 获取图片
url = 'http://www.netbian.com/mei/'
import requests
import re
from lxml import etree

hearders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
req = requests.get(url,headers=hearders)
req.encoding='gbk'  #中文显示

e = etree.HTML(req.text)

img_urls = e.xpath('//ul/li/a/img/@src')
img_names = e.xpath('//ul/li/a/img/@alt')

for u,n in zip(img_urls,img_names):
    # print(type(n.strip().replace('*','')))
    print(re.sub('\d','',n.strip().replace('*', '')))
    # print(n.strip().replace('*', '').join(c if not c.isnumeric() else '' for c in text))
    print(f'正在下载...图片名:{u} 地址:{n}')
    d = re.sub('\d', '', n.strip().replace('*', ''))
    reg_repo = requests.get(u,headers=hearders)
    with open(f'G:/picture/{d}.jpg','wb') as f:
        f.write(reg_repo.content)
    f.close()
# print(req.text)

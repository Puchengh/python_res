url = 'https://nba.hupu.com/stats/players'

import requests
from lxml import etree
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}
req = requests.get(url,headers = headers)
# print(req.text)

e = etree.HTML(req.text)
nums = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')
with open('G:/picture/compose/nba.txt','w',encoding='utf-8') as f:
    for num,name,team,score in zip(nums,names,teams,scores):
        f.write(f'${num}--${name}--${team}--${score} \n')
    f.close()
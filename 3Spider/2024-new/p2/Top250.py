import requests
import re
import csv

flag = True
page = 0
while flag:
    if (page > 226):
        flag = False

    url = f"https://movie.douban.com/top250?start={page}&filter="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }

    resp = requests.get(url, headers=headers)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                     r'<p class="">.*?<br>\n(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(page_content)

    f = open("data.csv", mode="a", encoding="utf-8")
    writer = csv.writer(f, lineterminator='\n')
    for name in result:
        # print(name.group("name") + " " + name.group("year").strip() + " " + name.group("score").strip() + " " + name.group(
        #     "num").strip())
        # print(name.group("name"))
        # print(name.group("year").replace("\n","").strip())
        # print(name.group("score"))
        # print(name.group("num"))

        dic = name.groupdict()
        dic['year'] = dic['year'].strip()
        dic['num'] = dic['num'].strip().replace("\n", "").strip()
        writer.writerow(dic.values())

    f.close()
    print(f"{page}-over!")
    # print(name.groupdict().values())
    # print(name.groupdict()['year'].replace("\n","").strip())
    page = page + 25


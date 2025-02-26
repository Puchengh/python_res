import requests
import re

domin = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

cookies = {
    "cookie": "__51vcke__KSHU1VNqce379XHB=69b7f46b-6689-529a-8b2d-fb9759e1695a; __51vuft__KSHU1VNqce379XHB=1722167075841; guardok=MgLq6vNSBH/QpI4wTnQukcaApHYuw9COQj1US9s7bAscbc4Gyo4hRunU23caQbdd7jCXRmCq/LjW9922bnGc5g==; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22b4138a6f-e391-55c3-81e2-58b607731cb7%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201722680605603%2C%20%22ct%22%3A%201722678805603%7D; __51uvsct__KSHU1VNqce379XHB=3; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1722167076,1722346793,1722678806; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1722678806; HMACCOUNT=E83668A7606446E1; Hm_lvt_8e745928b4c636da693d2c43470f5413=1722167076,1722346793,1722678806; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1722678806; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1722167076,1722346793,1722678806; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1722678806"
}
resp = requests.get(domin, verify=False, headers=headers, cookies=cookies)
resp.encoding = 'gb2312'
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(f"2024必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="'
                  r'(?P<download>.*?)">',re.S)
result = obj1.finditer(resp.text)

child_href_list = []
for it in result:
    ul = it.group('ul')
    hrefss = obj2.finditer(ul)
    for itt in hrefss:
        # 拼接子页面的url地址： 域名 + 子页面地址
        child_href = domin + itt.group('href').strip("/")
        child_href_list.append(child_href)

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False, headers=headers, cookies=cookies)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    # break   # 测试用

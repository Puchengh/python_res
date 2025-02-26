import requests
from lxml import etree as et
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '100',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'Cookies-01=59063098; ASP.NET_SessionId=cks2q15imd3fnaiade3l4yog; __jsluid_s=c02d0dcfe574ab9ffe5f4ff1f31f8f75; Hm_lvt_5698cdfa8b95bb873f5ca4ecf94ac150=1715146110; __jsl_clearance_s=1715146124.091|0|nV%2FCPN251HbiqemN5vagfWl0kJc%3D; Hm_lpvt_5698cdfa8b95bb873f5ca4ecf94ac150=1715147016',
    'Host': 'www1.rmfysszc.gov.cn',
    'Origin': 'https://www1.rmfysszc.gov.cn',
    'Referer': 'https://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
form_date = {'type': '0', 'name': '', 'area': '陕西省', 'city': '陕西省', 'city1': '==请选择==', 'city2': '==请选择==',
             'xmxz': '0', 'state': '0', 'money': '', 'money1': '', 'number': '0', 'fid1': '', 'fid2': '', 'fid3': '',
             'order': '0', 'page': '1', 'include': '0'}
req = requests.post('https://www1.rmfysszc.gov.cn/ProjectHandle.shtml', data=form_date, headers=headers)

print(req.text)

e = et.HTML(req.text)

titles = e.xpath('//div[@class="product"]/div[@class="p_img"]/a/@title')
info = e.xpath('//div[@class="product"]/div[2]/p[1]/text()')

prices1 = e.xpath('//div[@class="product"]/div[2]/p[1]/span/text()')  # 评估值
prices2 = e.xpath('//div[@class="product"]/p/strong/text()')  # 起拍价

issucc = e.xpath('//div[@class="prod-alink"]/a/text()')
# print(info)


for t,i,p1,p2,isc in zip(titles,info,prices1,prices2,issucc):
    str_is = ''
    if isc == '已成交':
        str_is = '成交价'
    else:
        str_is = '起拍价'
    print(f'名称：{t} --- {str_is}:{p2} --- {i}:{p1} ---是否已成交:{isc}')
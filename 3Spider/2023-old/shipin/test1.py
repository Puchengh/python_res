import requests   # 数据请求模块
import re     # 正则表达式模块
import json  # 数据类型处理模块
from tqdm import tqdm   #进度条配置
import os    # 处理文件和目录

headers = {
    'cookie': 'GPS=1; YSC=y8La2i2J8ss; VISITOR_INFO1_LIVE=kKz2VJzZhMw; VISITOR_PRIVACY_METADATA=CgJISxIEGgAgXA%3D%3D; PREF=f7=4000&tz=Asia.Shanghai',
    'referer': 'https://www.youtube.com/results?search_query=jk%E7%BE%8E%E5%A5%B3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
url = 'https://www.youtube.com/watch?v=b54oABKKV7E'

response = requests.get(url=url, headers=headers)

# re.findall()
# print(response.text)

json_str = re.findall('var ytInitialPlayerResponse = (.*?);var', response.text)[0]
# print(json_str)
#
json_data = json.loads(json_str)
video_url = json_data['streamingData']['adaptiveFormats'][0]
print(video_url)
# audio_url = json_data['streamingData']['adaptiveFormats'][-2]['url']
# title = json_data['videoDetails']['title']
#
# title = title.replace(' ', '')
#
# title = re.sub(r'[\/:|?*"<>]', '', title)
# print(video_url)
# print(audio_url)
# print(title)
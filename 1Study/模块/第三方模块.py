'''
第三方 pillow
pip install pillow
'''
import requests


response = requests.get('https://www.12306.cn/index/')
print(response.text)
import json
from urllib import request,parse
from lxpy import copy_headers_dict
url = 'https://movie.douban.com/j/chart/top_list?type=5&inter val_id=100%3A90&action=&start=0&limit=20'

headers ="""
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0
"""
headers = copy_headers_dict(headers) # 快捷格式化headers
req = request.Request(url=url,headers=headers) # 请求对象的定制
response = request.urlopen(req) #模拟浏览器向服务器发送请求
contend = response.read().decode("utf-8")
#open方法默认编码为gbk编码，所以需要改变编码格式为utf-8
with open('duban_top20.json','w',encoding='utf-8') as js:
    js.write(contend,indent=4)

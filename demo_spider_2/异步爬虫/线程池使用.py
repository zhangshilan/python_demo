# -*- codeing = utf-8 -*-
#@Time :2020/11/18 16:08
#@Author :张士澜
#@File :线程池使用.py
#@Software :PyCharm

from multiprocessing.dummy import Pool
import time
import requests

start_time = time.time()
headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
urls = [
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli13996.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli13987.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli13982.rar'
]

def get_content(url):
    print("正在爬取：",url)
    response = requests.get(url = url,headers = headers)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print('响应数据长度为：',len(content))

content_list = []
pool = Pool(3)
content_list =pool.map(get_content,urls)
for content in content_list:
    parse_content(content)

end_time = time.time()
print(end_time-start_time)
# -*- codeing = utf-8 -*-
#@Time :2021/1/3 17:59
#@Author :张士澜
#@File :COVID-19_spider.py
#@Software :PyCharm

import requests
import re

if __name__ =='__main__':
    url = 'https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish&callback=jsonp_1609725310779_99223'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    page_text = requests.get(url = url,headers = headers).text
    print(page_text)
    ex = 'jsonp_1609725310779_99223(.*?);'
    text = re.findall(ex,page_text,re.S)
    print(text)
    # response = requests.get(url = url,headers = headers)
    # json = response.json()
    # print(json)
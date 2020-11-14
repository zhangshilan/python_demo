# -*- codeing = utf-8 -*-
#@Time :2020/11/14 17:32
#@Author :张士澜
#@File :request_kfc.py
#@Software :PyCharm

import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    city = input('enter an city:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': city,
        'pageIndex': '1',
        'pageSize': '10'
    }

    response = requests.post(url = url,data = data,headers = headers)
    page_text = response.text

    filename = city+'.txt'
    fp = open(filename,'w',encoding='utf-8')
    fp.write(page_text)
    print('over')
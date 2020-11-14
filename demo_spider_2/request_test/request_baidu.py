# -*- codeing = utf-8 -*-
#@Time :2020/11/14 12:39
#@Author :张士澜
#@File :request_baidu.py
#@Software :PyCharm

import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    #post请求参数处理
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #进行UA伪装
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    #请求发送
    response = requests.post(url = post_url,data = data,headers = headers)
    #获取响应数据,json返回的是obj(如果确认响应数据是json类型才可以用json（）)
    dic_obj = response.json()
    print(dic_obj)
    #进行持久化存储
    filename = word + '.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp = fp,ensure_ascii=False)

    print("over")
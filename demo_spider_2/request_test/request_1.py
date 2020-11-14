# -*- codeing = utf-8 -*-
#@Time :2020/11/14 11:16
#@Author :张士澜
#@File :request_1.py
#@Software :PyCharm

import requests
if __name__ == "__main__":
    #step1:指定url
    url = 'https://www.sogou.com/'
    #step2:发起请求
    #get方法会获得一个响应对象
    response = requests.get(url = url)
    #step3:获取响应数据
    page_text = response.text         #返回字符串形式的响应数据
    print(page_text)
    #step4:持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp .write(page_text)
    print("爬取数据结束")
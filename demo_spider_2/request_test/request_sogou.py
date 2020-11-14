# -*- codeing = utf-8 -*-
#@Time :2020/11/14 12:13
#@Author :张士澜
#@File :request_sogou.py
#@Software :PyCharm


#UA监测：门户网站的服务器会监测对应请求的载体的身份标识，如果监测到位某一款浏览器，则表示这是一个正常请求，如果不是则该请求为不正常的请求，服务器端有可能拒绝该请求
#UA：User-Agent（请求载体的身份标识）
#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器，将对应的UA封装在字典中
import requests

if __name__ == "__main__":
    url = "https://www.sogou.com/web"
    #处理url携带的参数：封装到字典中
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url = url,params=param,headers = headers)

    page_text = response.text
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(filename,'保存成功！')

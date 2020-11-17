# -*- codeing = utf-8 -*-
#@Time :2020/11/17 14:43
#@Author :张士澜
#@File :xpath_picture.py
#@Software :PyCharm

#需求：爬取4k图片

import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    url = "http://pic.netbian.com/4kfengjing/"
    response = requests.get(url = url,headers = headers)
    #手动设定响应数据的编码格式
    # response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src = li.xpath('./a/img/@src')[0]
        img_url = "http://pic.netbian.com"+img_src
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        #通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url = img_url,headers = headers).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb',) as fp:
            fp.write(img_data)
            print(img_name,'下载成功！')

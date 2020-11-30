# -*- codeing = utf-8 -*-
#@Time :2020/11/17 17:11
#@Author :张士澜
#@File :xpath_ppt.py
#@Software :PyCharm

import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    header = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.102Safari / 537.36Edge / 18.18362'
    }
    if not os.path.exists('./PPTLibs'):
        os.mkdir('./PPTLibs')
    base_url = "http://www.1ppt.com/moban/jianjie/ppt_jianjie_1.html"
    for num in range(5):
        response = requests.get(url = base_url ,headers =header)
        # response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        print(page_text)
        li_list = tree.xpath('/html/body/div[6]/dl/dd/ul/li')
        for li_tree in li_list:
            new_url = "http://www.1ppt.com"+li_tree.xpath('./a/@href')[0]
            name = li_tree.xpath('./h2/a/text()')[0]+'.rar'
            new_text = requests.get(url = new_url,headers = headers).text
            new_tree = etree.HTML(new_text)
            download_url = "http://www.1ppt.com"+new_tree.xpath('/html/body/div[5]/div[1]/dl/dd/ul[1]/li/a/@href')[0]
            file_text = requests.get(url = download_url,headers = headers).text
            file_tree = etree.HTML(file_text)
            file_url = file_tree.xpath('/html/body/dl/dd/ul[2]/li[1]/a/@href')
            file = requests.get(url = file_url,headers = headers).content
            filepath = 'PPTLibs/'+name
            with open(filepath,'wb') as fp:
                fp.write(file)
                print(name,"下载成功！")


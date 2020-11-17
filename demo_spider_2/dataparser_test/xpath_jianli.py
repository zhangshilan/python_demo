# -*- codeing = utf-8 -*-
#@Time :2020/11/17 15:57
#@Author :张士澜
#@File :xpath_jianli.py
#@Software :PyCharm

import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    if not os.path.exists('./jianliLibs'):
        os.mkdir('./jianliLibs')
    base_url = "https://sc.chinaz.com/jianli/free_%d.html"
    for num in range(2,3):
        response = requests.get(url = base_url %num,headers =headers)
        response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        div_list = tree.xpath('//div[@id = "main"]/div/div')
        for div_tree in div_list:
            new_url = "http:"+div_tree.xpath('./a/@href')[0]
            name = div_tree.xpath('./p/a/text()')[0]+'.rar'
            new_text = requests.get(url = new_url,headers = headers).text
            new_tree = etree.HTML(new_text)
            download_url = new_tree.xpath('//div[@class = "clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
            file = requests.get(url = download_url,headers = headers).content
            filepath = 'jianliLibs/'+name
            with open(filepath,'wb') as fp:
                fp.write(file)
                print(name,"下载成功！")
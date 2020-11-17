# -*- codeing = utf-8 -*-
#@Time :2020/11/17 10:48
#@Author :张士澜
#@File :xpath_58.py
#@Software :PyCharm

#需求：爬取58二手房中的房源信息

from lxml import etree
import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }

    url = "https://bd.58.com/ershoufang/"
    page_text = requests.get(url = url,headers = headers).text
    fp = open('58.txt','w',encoding='utf-8')
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class = "house-list-wrap"]/li')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        sum = li.xpath('./div[3]/p[@class = "sum"]//text()')[0]
        #print(title)
        fp.write(title+'\n'+sum+'万\n')
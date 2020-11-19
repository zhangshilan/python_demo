# -*- codeing = utf-8 -*-
#@Time :2020/11/13 15:50
#@Author :张士澜
#@File :cloudmusic_spider.py
#@Software :PyCharm

import requests
from lxml import etree
import os

if __name__ == '__main__':
    if not os.path.exists('./music'):
        os.mkdir('./music')
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url = 'https://music.163.com/discover/toplist'
    page_text = requests.get(url = url,headers = headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="f-hide"]/li')
    for li in li_list:
        name = li.xpath('./a/text()')[0]
        detail_url = "https://music.163.com/#"+li.xpath('./a/@href')[0]
        detail_text = requests.get(url = detail_url,headers = headers).text
        detail_tree = etree.HTML(detail_text)
        lyric = detail_tree.xpath('//div[@id="lyric-content"]//text()')
        # filepath = "music/"+name+".txt"
        # with open(filepath,'w',encoding='utf-8') as fp:
        #     fp.write(lyric)
        print(detail_text)
        print(name,"歌词下载完毕")
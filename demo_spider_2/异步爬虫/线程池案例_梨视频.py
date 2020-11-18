# -*- codeing = utf-8 -*-
#@Time :2020/11/18 16:30
#@Author :张士澜
#@File :线程池案例_梨视频.py
#@Software :PyCharm

#需求：爬取梨视频的视频数据
#原则：线程池处理的是阻塞且耗时的操作

import requests
from multiprocessing.dummy import Pool
from lxml import etree
import random

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url = url,headers = headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id = "listvideoListUl"]/li')
    detail_list = []
    for li in li_list:
        detail_url = "https://www.pearvideo.com/"+li.xpath('./div/a/@href')[0]
        # detail_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1707447&mrd=0.3638348795661084'
        name = li.xpath('./div/a/div[2]/text()')[0]+'.html'
        dic = {
            'name':name,
            'url':detail_url
        }
        detail_list.append(dic)
        #print(detail_url,name)
        # contId = li.xpath('./div/div/span/@data-id')[0]
        # data ={
        #     'contId': contId,
        #     'mrd':random.random()
        # }
        # response = requests.get(url = detail_url,data = data,headers = headers)
        # json_detail = response.json()
        # mp4_url = json_detail.videoInfo.videos.srcUrl
    def get_video_text(dic):
        url = dic['url']
        video_text = requests.get(url = url ,headers = headers).text
        with open(dic['name'],'w',encoding='utf-8') as fp:
            fp.write(video_text)
            print(dic['name'],"保存成功！")
    pool = Pool(4)
    pool.map(get_video_text,detail_list)

    pool.close()
    pool.join()
# -*- codeing = utf-8 -*-
#@Time :2020/11/15 11:06
#@Author :张士澜
#@File :re_test.py
#@Software :PyCharm

#需求:爬取糗事百科界面下全部的图片
import requests
import re
import os
if __name__ == '__main__':
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    #设计一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1,14):
        new_url = format(url%pageNum)
        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url = new_url,headers = headers).text

        #使用聚焦爬虫将页面中所有的图片进行解析提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        print(img_src_list)
        for src in img_src_list:
            #拼接出一个完整的图片url
            src = 'https:'+src
            img_data = requests.get(url = src,headers = headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            #图片存储的路径
            imgPath = './qiutuLibs/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！')
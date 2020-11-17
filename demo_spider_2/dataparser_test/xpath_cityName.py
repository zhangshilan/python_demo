# -*- codeing = utf-8 -*-
#@Time :2020/11/17 15:18
#@Author :张士澜
#@File :xpath_cityName.py
#@Software :PyCharm

import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    url = "https://www.aqistudy.cn/historydata/"
    page_text = requests.get(url = url,headers = headers).text
    tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class = "bottom"]/ul/li')
    # hot_city_names = []
    # all_city_names = []
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     hot_city_names.append(hot_city_name)
    # all_li_list = tree.xpath('//div[@class = "bottom"]/ul/div[2]/li')
    # for li in all_li_list:
    #     all_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(all_city_name)
    # print("热门城市:",hot_city_names,'\n',"全部城市：",all_city_names)
    all_city_names = []
    a_list = tree.xpath('//div[@class = "bottom"]/ul/li/a | //div[@class = "bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names)
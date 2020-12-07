# -*- codeing = utf-8 -*-
#@Time :2020/12/7 9:30
#@Author :张士澜
#@File :baidu_hot.py
#@Software :PyCharm

import requests
from lxml import etree
import os
import datetime
import xlwt,xlrd

def saveData(datalist,savepath,date):
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet(date,cell_overwrite_ok=True)  # 创建工作表
    col = ("排名","关键词","热度")
    for i in range(0,3):
        worksheet.write(0,i,col[i])
    for i in range(0,50):
        data = datalist[i]
        for j in range(0,3):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

if __name__ == "__main__":
    month = datetime.datetime.now().strftime('%Y年%m月')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    document = "./"+month+"热搜排行榜"
    print(month)
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }

    url = "http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1"
    if not os.path.exists(document):
        os.mkdir(document)
    filepath = document+'/'+date+'热搜排行榜.xls'
    # print(filepath)
    response = requests.get(url = url,headers = headers)
    response.encoding = 'gbk'
    hot_page = response.text
    tree = etree.HTML(hot_page)
    # print(hot_page)
    tr_list = tree.xpath('//table[@class = "list-table"]//tr')
    # print(tr_list)
    data_list = []
    for tr in tr_list[1:]:
        first = tr.xpath('./td[1]/span/text()')[0]
        keyword = tr.xpath('./td[2]/a/text()')[0]
        last = tr.xpath('./td[4]/span/text()')[0]
        detail = [first,keyword,last]
        # print(first,"  ",keyword,"  ",last,"\n")
        data_list.append(detail)
    # print(data_list)
    saveData(data_list,filepath,date)
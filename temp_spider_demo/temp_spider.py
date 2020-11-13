# -*- codeing = utf-8 -*-
#@Time :2020/11/10 10:39
#@Author :张士澜
#@File :temp_spider.py
#@Software :PyCharm


import sys
import re
import urllib.request,urllib.error
import xlwt
from bs4 import BeautifulSoup
import sqlite3

findLi = re.compile(r'<li class=(.*?)</li>')
findDate = re.compile(r'<h1>(.*?)</h1>')
findWea = re.compile(r'<p class="wea" title="(.*)">')
findMaxTemp = re.compile(r'<span>(.*?)</span>')
findMinTemp = re.compile(r'<i>(.*?)</i>')

def getData(baseurl):
    datalist = []
    html = askURL(baseurl)

    soup = BeautifulSoup(html,"html.parser")
    ul = soup.find('ul', class_ = "t clearfix")
    li = ul.find_all('li')
    #print(li)
    for item in li:

        data = []
        item = str(item)
        date = re.findall(findDate,item)[0]
        data.append(date)

        wea = re.findall(findWea,item)[0]
        data.append(wea)

        maxtemp = re.findall(findMaxTemp,item)
        if len(maxtemp) != 0:
            data.append(maxtemp)
        else:
            data.append(" ")
        # data.append(maxtemp)

        mintemp = re.findall(findMinTemp,item)[0]
        if len(mintemp) != 0:
            data.append(mintemp)
        else:
            data.append(" ")
        # data.append(mintemp)

        datalist.append(data)
    # print(li)
    print(datalist)
    return datalist





def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.183Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
    #print("...")


def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet = workbook.add_sheet("保定七天天气状况",cell_overwrite_ok=True)
    col = ("日期","天气状况","最高气温","最低气温")
    for i in range(0,4):
        worksheet.write(0,i,col[i])
    for i in range(0,7):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,4):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

def saveData2DB(datalist,dbpath):
    #init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    value = []
    for index in range(0,7):
        data = tuple(datalist[index])
        value.append(data)

    sql = '''
                insert into temp7(
                date,temp,maxtemp,mintemp) 
                values(?,?,?,?)'''
    print(value)
    cur.executemany(sql,value)
    conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
    create table temp7
    (id integer primary key autoincrement,
    date text,
    temp text,
    maxtemp text,
    mintemp text
    )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def main():
    baseurl = "http://www.weather.com.cn/weather/101090201.shtml"
    savepath = "temp.xls"
    dbpath = "temp.db"

    datalist = getData(baseurl)
    saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)

main()
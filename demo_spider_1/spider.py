# -*- codeing = utf-8 -*-
# @Time :2020/11/4 19:43
# @Author :张士澜
# @File :spider.py
# @Software :PyCharm


#import sys
import re                          #正则表达式，进行文字匹配
import urllib.request,urllib.error #制定URL，获取网页数据
import xlwt                        #进行excel操作
from bs4 import BeautifulSoup      #网页解析，获取数据
import sqlite3                     #进行SQLite数据库操作

# 1.爬取网页
# 2.解析数据
# 3.保存数据

findLink = re.compile(r'<a href="(.*?)">')      #创建正则表达式对象，表示规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)    #re.S让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):          #调用获取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)         #保存获取到的网页源码

        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink,item)[0] #获取影片详情链接
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judge = re.findall(findJudge,item)[0]
            data.append(judge)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())

            datalist.append(data)

    return datalist

#得到指定一个URL网页的内容
def askURL(url):
    head = {               #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
                           #用户代理，告诉豆瓣服务器我们是什么样的机器、浏览器（本质上是告诉浏览器我们是什么水平的文档）
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
       # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#保存数据
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

    print("save succeed......")



def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range (len(data)):
            if index == 4 or index ==5:
                continue
            data[index] = '"' +data[index]+'"'
        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text)
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



def main():
    baseurl = 'https://movie.douban.com/top250?start='
    #savepath = "豆瓣电影TOP250.xls"
    dbpath = "movie.db"
    datalist = getData(baseurl)
    print("爬取完毕")
    #print(datalist)
    # askURL("https://movie.douban.com/top250?start=0")
    #saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)

main()

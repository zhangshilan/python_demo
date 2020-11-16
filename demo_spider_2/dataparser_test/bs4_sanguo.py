# -*- codeing = utf-8 -*-
#@Time :2020/11/16 10:50
#@Author :张士澜
#@File :bs4_sanguo.py
#@Software :PyCharm

#爬取三国演义所有的章节标题和章节内容https://www.shicimingju.com/book/sanguoyanyi.html

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    #对首页页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url = url,headers = headers).text

    #在首页中解析出章节的标题和详情页的url
    #1、实例化BeautifulSoup对象，将页面源码加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li ')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        detail_text = requests.get(url = detail_url,headers = headers).text
        detail_soup = BeautifulSoup(detail_text,'lxml')
        div_tag = detail_soup.find('div',class_ = 'chapter_content')
        content = div_tag.text
        fp.write(title+'\n'+content+'\n')
        print(title,'爬取成功！')
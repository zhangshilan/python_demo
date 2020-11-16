# -*- codeing = utf-8 -*-
#@Time :2020/11/16 10:09
#@Author :张士澜
#@File :bs4_test.py
#@Software :PyCharm


from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open('./douban.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.a)
    # print(soup.find('a'))
    # print(soup.find('div',class_ = 'tagslist').string)
    # print(soup.find_all('a'))
    # print(soup.select('.mod'))
    print(soup.select('.tagslist > ul a')[0]['href'])
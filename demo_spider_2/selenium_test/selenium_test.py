# -*- codeing = utf-8 -*-
#@Time :2020/11/22 10:45
#@Author :张士澜
#@File :selenium_test.py
#@Software :PyCharm

from selenium import webdriver
from lxml import etree
from time import sleep
# #实例化一个浏览器对象
# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# #让浏览器发起一个指定url的请求
# bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# #获取浏览器当前页面的源码数据
# page_text = bro.page_source
# tree = etree.HTML(page_text)
# li_list = tree.xpath('//ul[@id = "gzlist"]/li')
# for li in li_list:
#     name = li.xpath('./dl/@title')[0]
#     print(name)
# sleep(5)
# bro.quit()

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('http://www.taobao.com/')
search_input = bro.find_element_by_id('q')    #标签定位
search_input.send_keys('huawei')        #标签定位
#执行一组js代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(5)
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()        #点击搜索按钮
bro.get('https://www.baidu.com')
sleep(2)
bro.back()
sleep(2)
bro.forward()
sleep(5)
bro.quit()

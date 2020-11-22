# -*- codeing = utf-8 -*-
#@Time :2020/11/22 14:35
#@Author :张士澜
#@File :谷歌无头浏览器.py
#@Software :PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  #实现无可视化界面
from time import sleep
from selenium.webdriver import ChromeOptions   #实现规避检测

#实现无可视化界面的操作
#实例化一个option对象
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实现让selenium规避被检测的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-qutomation'])
bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options = chrome_options,options = option)

bro.get('http://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()
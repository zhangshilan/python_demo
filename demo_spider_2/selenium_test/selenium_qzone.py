# -*- codeing = utf-8 -*-
#@Time :2020/11/22 13:09
#@Author :张士澜
#@File :selenium_qzone.py
#@Software :PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('1845811424')
sleep(1)
password_tag.send_keys('')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()
sleep(2)   #等待页面加载
# bro.switch_to.frame('tcaptcha_iframe')
# block = bro.find_element_by_id('tcaptcha_drag_thumb')
# action = ActionChains(bro)
# action.click_and_hold(block)
# action.move_by_offset(178,0).perform()
# action.release()

# sleep(3)
# bro.quit()
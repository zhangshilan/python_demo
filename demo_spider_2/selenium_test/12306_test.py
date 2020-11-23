# -*- codeing = utf-8 -*-
#@Time :2020/11/22 15:27
#@Author :张士澜
#@File :12306_test.py
#@Software :PyCharm

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
            self.username = username
            password =  password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


# chaojiying = Chaojiying_Client('shilan', 'zhangshilan1995', '910025')
# im = open('12306.jpg', 'rb').read()
# print(chaojiying.PostPic(im, 9004)['pic_str'])

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from PIL import Image

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.maximize_window()
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
a_tag = bro.find_element_by_class_name('login-hd-account')
a_tag.click()
time.sleep(2)

bro.save_screenshot('a.png')
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location
size = code_img_ele.size
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

i = Image.open('./a.png')
code_img_name = './code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

chaojiying = Chaojiying_Client('shilan', 'zhangshilan1995', '910025')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)

else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(xy_list)
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
    time.sleep(2)

bro.find_element_by_id('J-userName').send_keys('xxxxxx')
time.sleep(1)
bro.find_element_by_id('J-password').send_keys('xxxxx')
time.sleep(1)
bro.find_element_by_id('J-login').click()
time.sleep(5)
bro.quit()
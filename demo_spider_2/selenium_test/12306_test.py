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
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
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
code_img_name = 'code.png'
frame = i.crop(rangle)
frame.save(code_img_name)
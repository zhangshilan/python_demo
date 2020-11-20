# -*- codeing = utf-8 -*-
#@Time :2020/11/20 17:09
#@Author :张士澜
#@File :asyncio+requests.py
#@Software :PyCharm

import asyncio
import requests
import os

async def download_image(url):
    print("开始下载",url)
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None,requests.get,url)
    response = await future
    print("下载完成")
    file_name = url.rsplit('/')[-1]
    with open(file_name,'wb') as fp:
        fp.write(response.content)

if __name__ == '__main__':
    url_list = [
        'http://pic.netbian.com/uploads/allimg/201028/223051-1603895451cb94.jpg',
        'http://pic.netbian.com/uploads/allimg/190217/185005-155040060514a6.jpg',
        'http://pic.netbian.com/uploads/allimg/170930/104047-15067392476f35.jpg'
    ]
    tasks = [download_image(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait(tasks) )
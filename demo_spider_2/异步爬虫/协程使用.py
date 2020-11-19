# -*- codeing = utf-8 -*-
#@Time :2020/11/19 15:23
#@Author :张士澜
#@File :协程使用.py
#@Software :PyCharm

import asyncio

async def request(url):
    print('正在请求的url是：',url)
    print('请求成功',url)
#async修饰的函数，调用之后返回一个协程对象
c =request('www.baidu.com')

loop = asyncio.get_event_loop()
#将协程对象注册到loop中，然后启动loop
loop.run_until_complete(c)

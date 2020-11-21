# -*- codeing = utf-8 -*-
#@Time :2020/11/21 13:07
#@Author :张士澜
#@File :aiohttp_test.py
#@Software :PyCharm

import asyncio
import aiohttp
import time

start = time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.douban.com'
]
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据，read（）返回二进制形式的响应数据，json()返回json对象
            page_text = await response.text()
            print(len(page_text))

tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()

print("总耗时：",end-start)
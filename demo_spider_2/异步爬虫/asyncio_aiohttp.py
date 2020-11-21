# -*- codeing = utf-8 -*-
#@Time :2020/11/21 11:42
#@Author :张士澜
#@File :asyncio_aiohttp.py
#@Software :PyCharm

import asyncio
import aiohttp

async def fetch(session,url):
    print("发送请求",url)
    async with session.get(url,verify_ssl = False) as response:
        text = await response.text()
        print("得到结果",url,len(text))
        return text

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'http://www.baidu.com',
            'http://python.org',
            'http://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session,url)) for url in url_list]

        done,pending = await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())
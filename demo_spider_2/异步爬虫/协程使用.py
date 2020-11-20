# -*- codeing = utf-8 -*-
#@Time :2020/11/19 15:23
#@Author :张士澜
#@File :协程使用.py
#@Software :PyCharm

# import asyncio
#
# async def request(url):
#     print('正在请求的url是：',url)
#     print('请求成功',url)
# #async修饰的函数，调用之后返回一个协程对象
# c =request('www.baidu.com')
#
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)


import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")
    # 创建task对象，将当前执行的func函数任务添加到事件循环。
    task_list = [
        asyncio.create_task(func(),name = 'n1'),
        asyncio.create_task(func(),name = 'n2')
    ]
    print("main结束")

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


asyncio.run(main())
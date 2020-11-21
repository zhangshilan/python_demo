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


# import asyncio
#
# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return "返回值"
#
# async def main():
#     print("main开始")
#     # 创建task对象，将当前执行的func函数任务添加到事件循环。
#     task_list = [
#         asyncio.create_task(func(),name = 'n1'),
#         asyncio.create_task(func(),name = 'n2')
#     ]
#     print("main结束")
#
#     done, pending = await asyncio.wait(task_list, timeout=None)
#     print(done)
#
# asyncio.run(main())

#多任务协程
import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    #time.sleep(2)
    await asyncio.sleep(2)    #在asyncio中遇到阻塞操作必须进行手动挂起
    print('下载完毕',url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.douban.com'
]

#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
#将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

end = time.time()
print(end-start)
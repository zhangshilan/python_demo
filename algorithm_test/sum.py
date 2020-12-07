# -*- codeing = utf-8 -*-
#@Time :2020/12/5 21:10
#@Author :张士澜
#@File :sum.py
#@Software :PyCharm

# def sum(arr):
#     if not arr:
#         return 0
#     else:
#         return arr.pop() + sum(arr)

def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])

list = [2,4,6]
print(sum(list))
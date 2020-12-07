# -*- codeing = utf-8 -*-
#@Time :2020/12/6 11:02
#@Author :张士澜
#@File :quick_sort.py
#@Software :PyCharm

#快速排序，使用分治策略，时间复杂度是O（n logn）
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]    #列表推导式
        greater = [i for i in list[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

x = input(r"input a list splitted with ',':")
list = x.split(",")
my_list = [int(list[i]) for i in range(len(list))]
# list = [7,66,1,35,26,15]
print(quicksort(list))
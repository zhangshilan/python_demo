# -*- codeing = utf-8 -*-
#@Time :2020/12/5 16:58
#@Author :张士澜
#@File :selection_sort.py
#@Software :PyCharm


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

def selectionSort_small(arr):
    new_arr1 = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        new_arr1.append(arr.pop(smallest_index))
    return new_arr1

def selectionSort_big(arr):
    new_arr2 = []
    for i in range(len(arr)):
        biggest_index = findBiggest(arr)
        new_arr2.append(arr.pop(biggest_index))
    return new_arr2

list = [5,3,7,1,8,4]

# print(selectionSort_big(list))
print(selectionSort_small(list))
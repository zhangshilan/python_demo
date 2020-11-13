# -*- codeing = utf-8 -*-
# @Time :2020/11/5 16:05
# @Author :张士澜
# @File :bs4test.py
# @Software :PyCharm

'''
Beautifulsoup4将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可归纳为四种：
-Tag-标签及其内容：拿到它所找到的第一个内容
-NavigableString-标签里的内容
-BeautifulSoup-整个文档
-Comment-注释，是一个特殊的navigablestring，输出的内容不包括注释符号
'''

from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# print(bs.a)

# print(bs.head)
# print(type(bs.head))

# print(bs.title.string)
# print(type(bs.title.string))

# print(bs.a.attrs)
# print(type(bs.a.attrs))     #拿到标签里的所有属性

# print(bs.name)
# print(bs)
# print(type(bs))

# print(bs.a.string)
# print(type(bs.a.string))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#文档的遍历
#print(bs.head.contents)
#print(bs.head.contents[1])

#文档的搜索
#1、find_all()
#字符串过滤，查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
#正则表达式搜索：使用search（）方法来匹配内容
#t_list = bs.find_all(re.compile("a"))
#方法：传入一个函数fanc（），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

#2、kwargs  参数

#t_list = bs.find_all(href = True)

# for item in t_list:
#     print(item)

#3、text参数

#t_list = bs.find_all(text = ["地图","贴吧","更多"])
# t_list = bs.find_all(text = re.compile("\d"))
# for item in t_list:
#     print(item)

#4、limit参数
# t_list = bs.find_all("a",limit = 3)
# for item in t_list:
#     print(item)

#5、css选择器
# t_list = bs.select('title')     #按标签查找
# t_list = bs.select('.mnav')      #按类名查找
#t_list = bs.select('#u1')          #按id查找
#t_list = bs.select("a[class='mnav']")  #按属性查找
# t_list = bs.select("head>title")        #按子标签查找
# for item in t_list:
#     print(item)
t_list= bs.select(".mnav ~ .bri")     #按兄弟标签查找
print(t_list[0].get_text())
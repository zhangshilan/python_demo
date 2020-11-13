# -*- codeing = utf-8 -*-
# @Time :2020/11/6 15:24
# @Author :张士澜
# @File :re_test.py
# @Software :PyCharm


#正则表达式：字符串模式，判断字符串是否符合一定的标准
#建议在正则表达式，被比较的字符串前加上r，不用担心转义字符的问题
import re

pat = re.compile("AA")  #此处的AA是正则表达式，用来验证其他的字符串
#m = pat.search("ABCAA")       #search字符串后被校验的内容,search方法进行查找比对
#m = pat.search("ABCAADDCCAAA")

# m = re.search("asd","Aasd")     #前面的字符串是规则，后面的字符串是被检验对象
# print (m)

#print(re.findall("a","ASDafgba"))  #前面的字符串是规则，后面的字符串是被校验对象

# print(re.findall("[A-Z]","afFAGafgFS"))
# print(re.findall("[A-Z]+","afFAGafgFS"))

print(re.sub("a","A","abcdasd"))     #用第二个字符串替换第一个字符串
# -*- codeing = utf-8 -*-
# @Time :2020/11/7 10:54
# @Author :张士澜
# @File :dbTest.py
# @Software :PyCharm

import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
# -*- codeing = utf-8 -*-
#@Time :2020/12/11 20:43
#@Author :张士澜
#@File :connect_test.py
#@Software :PyCharm

import pymysql

user = input('user:').strip()
pwd = input('password:').strip()

#建立链接
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'zsl1995',
    db = 'test',
    charset = 'utf8'
)
#拿到游标
cursor = conn.cursor()

#执行sql语句
# sql = 'select * from userinfo where user = "%s" and password = "%s"' %(user,pwd)
sql = 'select * from userinfo where user = %s and password = %s'
rows = cursor.execute(sql,(user,pwd))

cursor.close()
conn.close()

if rows:
    print("登录成功")
else:
    print("登录失败")
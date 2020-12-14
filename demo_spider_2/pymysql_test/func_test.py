# -*- codeing = utf-8 -*-
#@Time :2020/12/12 10:12
#@Author :张士澜
#@File :func_test.py
#@Software :PyCharm

import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'zsl1995',
    db = 'test',
    charset = 'utf8'
)
cursor = conn.cursor()
#增删改
# sql = 'insert into userinfo(user,password) values(%s,%s)'
# # rows = cursor.execute(sql,('wxx','123'))
# rows = cursor.executemany(sql,[('sdf','123'),('asf','134'),('aee','436')])
# print(rows)
# conn.commit()      #进行增删改之后必须执行提交步骤

#查询
cursor1 = conn.cursor(pymysql.cursors.DictCursor)
rows = cursor1.execute('select * from userinfo;')
# print(cursor1.fetchone())
# print(cursor1.fetchmany(3))
# print(cursor1.fetchall())

#游标移动
# cursor1.scroll(3,mode='absolute')   #相对绝对位置移动
print(cursor1.fetchone())
cursor1.scroll(3,mode='relative')   #相对当前位置移动
print(cursor1.fetchone())

cursor.close()
conn.close()


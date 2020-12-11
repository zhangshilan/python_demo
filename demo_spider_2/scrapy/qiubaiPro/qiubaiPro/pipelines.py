# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    fp = None
    #重写父类的一个方法，该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print("开始爬虫")
        self.fp = open('./qiubai.txt','w',encoding='utf-8')
    #专门处理item类型对象
    #该方法可以接收爬虫文件提交过来的item对象
    #该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')
        return item
    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()

class mysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host = '10.61.19.241',port = 3306,user = 'root',password = 'zsl1995',db = 'qiubai',charset = 'utf8')
        self.cursor = self.conn.cursor()
    def process_item(self,item,spider):

        try:
            self.cursor.execute('insert into qiubai(作者,内容) values("%s","%s")'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


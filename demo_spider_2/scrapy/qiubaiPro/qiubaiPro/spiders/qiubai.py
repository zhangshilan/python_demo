import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     print(response)
    #     all_data = []
    #     #解析：作者的名称和段子内容
    #     div_list = response.xpath('//div[@class = "main"]/div[1]/div[2]/div')
    #     for div in div_list:
    #         #xpath返回的是列表，但是列表元素一定是selector类型的对象
    #         #extract（）可以将selector对象中的data参数存储的字符串提取出来
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         #列表调用了extract()表示将列表中每一个selector对象中data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         # print(author,content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        print(response)
        all_data = []
        #解析：作者的名称和段子内容
        div_list = response.xpath('//div[@class = "main"]/div[1]/div[2]/div')
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是selector类型的对象
            #extract（）可以将selector对象中的data参数存储的字符串提取出来
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            #列表调用了extract()表示将列表中每一个selector对象中data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item #将item提交给管道

import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/dongwutupian.html']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # src = "https:"+div.xpath('./div/a/img/@src2').extract_first()      #使用为属性
            src_0 = src = div.xpath('./div/a/img/@src2').extract_first().split('_')[0]
            # print(src_0)
            src = "https:"+src_0+".jpg"
            item = ImgsproItem()
            item['src'] = src

            yield item

import scrapy
from lxml import etree

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.zhipin.com/c101010100/?query=python&ka=sel-city-101010100']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html']

    def parse_detail(self,response):
        job_desc = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)

    def parse(self, response):
        print(response)
        content = response.body.decode('utf-8')
        tree = etree.HTML(content)
        div_list = tree.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div')
        print(div_list)
        for div in div_list:
            job_name = div.xpath('./a/p/span/text()').extract_first()
            print(job_name)
            detail_url = div.xpath('./a/@href').extract_first()
            yield scrapy.Request(url = detail_url,callback = self.parse_detail)
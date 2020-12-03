import scrapy
from lxml import etree

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&ka=sel-city-101010100']

    def parse_detail(self,response):
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)

    def parse(self, response):
        print(response)
        content = response.body.decode('utf-8')
        tree = etree.HTML(content)
        li_list = tree.xpath('//div[@class="job-list"]/ul/li')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('.//div[@class = "job-name"]/a/text()').extract_first()
            print(job_name)
            detail_url = "https://www.zhipin.com"+li.xpath('.//div[@class = "job-name"]/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback = self.parse_detail)
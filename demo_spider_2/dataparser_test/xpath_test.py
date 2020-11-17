# -*- codeing = utf-8 -*-
#@Time :2020/11/17 9:50
#@Author :张士澜
#@File :xpath_test.py
#@Software :PyCharm

from lxml import etree

if __name__ == "__main__":
    #实例化了一个etree对象，并将需要解析的源码加载到对象中
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('douban.html',parser = parser)
    #r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="mod"]')
    # r = tree.xpath('//div[@class = "tagslist"]/ul/li[2]/a/text()')[0]
    # r = tree.xpath('//div[@class = "tagslist"]//text()')
    r = tree.xpath('//span[@class = "pl"]/a/@href')
    print(r)

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    user_agent_list = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        " Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        " Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    ]
    PROXY_http = [
        '153.180.102.104:80',
        '195.108.131.189:56055'
    ]
    PROXY_https = [
        '120.83.49.90:9000',
        '95.189.112.214:35508'
    ]
    #拦截请求
    def process_request(self, request, spider):
        #UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        request.meta['proxy'] = 'http://110.88.30.71:4245'
        return None
    #拦截所有响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
    #拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        if request.url.split(':')[0] == 'http':
        #代理
            request.meta['proxy'] = 'http://'+random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://'+random.choice(self.PROXY_https)

        return request  #将修正之后的对象进行重新的请求发送


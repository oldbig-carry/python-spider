import scrapy

class ComicSpider(scrapy.Spider):

    name = "comic"
    allowed_domains = ['http://www.1kkk.com/']
    start_urls = ['http://www.1kkk.com/manhua10684/']

    def parse(self, response):
        #link_urls = response.xpath('//*[@id="cp_a1"]/ul[3]/li/a[1]/@href').extract()
        dir_names = response.xpath('//*[@id="cp_a1"]/ul[3]/li/a[1]/text()').extract()
        for each_link in dir_names:
            print('http://www.1kkk.com' + each_link)
# -*- coding: utf-8 -*-
import scrapy


class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['theplantlist.org']
    start_urls = ['http://theplantlist.org/1.1/browse/']

    def parse(self,response):
        next_url = response.xpath('//*[@id="nametree"]/li/a/@href').extract()
        for i in next_url:
             url_a = 'http://theplantlist.org' + str(i)
             yield response.follow(url_a, self.parse_next) #this is following parse_next


    def parse_next(self,response):
            links_a = response.xpath('//*[@id="nametree"]/li/a/@href').extract()

            for k in links_a:
                url_c = 'http://theplantlist.org' + str(k)
                yield response.follow(url_c,self.parse_next1)

    def parse_next1(self,response):

        links = response.xpath('//ul[@class="nametree"]/li/a/@href').extract()

        for i in links:

             url_d = 'http://theplantlist.org' + str(i)

             yield response.follow(url_d, self.parse_nexturl2)

    def parse_nexturl2(self,response):
        data_url = response.xpath('//td[@class="name Unresolved"]/a/@href').extract()
        for i in data_url:
            url_d = 'http://theplantlist.org' + str(i)
            yield response.follow(url_d, self.parse_data)



    def parse_data(self,response):

        name1 = response.xpath('//ul[@class="bread"]/li/ul/li/a/i/text()').extract()
        name1 = ','.join(name1)
        name2 = response.xpath('//ul[@class="bread"]/li/ul/li/ul/li/a/i/text()').extract()
        name2 = ','.join(name2)
        name3 = response.xpath('//ul[@class="bread"]/li/ul/li/ul/li/ul/li/a/i/text()').extract()
        name3 = ','.join(name3)

        name4_a = response.xpath('//ul[@class="bread"]/li/ul/li/ul/li/ul/li/ul/li/span/i/text()').extract()
        name4_a = ' '.join(name4_a)

        name4_b = response.xpath('//ul[@class="bread"]/li/ul/li/ul/li/ul/li/ul/li/span/span/text()').extract()
        name4_b = ''.join(name4_b)

        fullname = name1 + ' -> ' + name2 + ' -> ' + name3 + ' -> ' + name4_a + ' ' + name4_b
        file = open("data.txt", "a+")
        print(fullname)
        file.write(fullname + "\n")

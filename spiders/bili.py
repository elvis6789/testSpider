# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
from testSpider.items import TestspiderItem

class biliSpider(scrapy.Spider):
    name = "bili"
    allow_domains = ['https://bangumi.bilibili.com']

    start_urls = ['https://bangumi.bilibili.com/api/season/v2/recommend?appkey=1d8b6e7d45233436&build=5240000&mobi_app=android&platform=android&season_id=23841&season_type=1&ts=1523783577&sign=164edbe2e7a9e9bd2ea1edf0bc1f7663']

    def parse(self, response):
        date_list = json.loads(response.body)['result']['list']

        #print("=========8888888888888888888888888888===")
        #print(str(date_list))
        
        
        for data in date_list:
            item = TestspiderItem()
            item['title'] = data['title']
            print("============")
            print("******item['title'] *****", item['title'])
            print("============")
            print ('ss')

            yield item
        

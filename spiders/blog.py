# -*- coding: utf-8 -*-
import scrapy
from EastmoneySpider.items import DemoItem


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['yezhwi.github.io']
    start_urls = ['https://yezhwi.github.io']

    def parse(self, response):
        for sel in response.xpath('//div[@class="post-preview"]'):
            item = DemoItem()
            item['title'] = sel.xpath('.//h2/text()').extract()
            item['link'] = sel.xpath('.//a/@href').extract()
            yield item

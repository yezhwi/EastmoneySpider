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
            # return list
            # item['title'] = sel.xpath('.//h2/text()').extract()
            item['title'] = sel.xpath('.//h2/text()').extract_first("").strip()
            item['link'] = response.url + sel.xpath('.//a/@href').extract_first("")
            yield item
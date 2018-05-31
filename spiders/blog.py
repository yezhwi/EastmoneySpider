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
            # extract()返回的也是一个列表
            # item['title'] = sel.xpath('.//h2/text()').extract()
            # extract_first()可以直接返回第一个值，extract_first()有一个参数default,如：extract_first(default="")表示如果匹配不到返回一个空
            item['title'] = sel.xpath('.//h2/text()').extract_first("").strip()
            item['link'] = response.url + sel.xpath('.//a/@href').extract_first("")
            yield item
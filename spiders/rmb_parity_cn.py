# -*- coding: utf-8 -*-
import scrapy
from EastmoneySpider.items import RMBExchangeRateItem


class RmbParityCnSpider(scrapy.Spider):
    name = 'rmb_parity_cn'
    allowed_domains = ['chinamoney.com.cn']
    start_urls = ['http://www.chinamoney.com.cn/r/cms/www/chinamoney/html/cn/latestRMBParityCn.html']

    def parse(self, response):
        # print response.body
        for sel in response.xpath('//table[@id="latest-rmb-parity-cn-list"]/tbody/tr'):
            item = RMBExchangeRateItem()
            # extract()返回的也是一个列表
            # item['title'] = sel.xpath('.//h2/text()').extract()
            # extract_first()可以直接返回第一个值，extract_first()有一个参数default,如：extract_first(default="")表示如果匹配不到返回一个空
            tags = sel.xpath('.//td[contains(@class, "left newcenter")]/text()').extract()
            item['currency_pair'] = tags[1]
            item['currency_pair_code'] = tags[1]
            item['ex_rate'] = tags[2]
            yield item

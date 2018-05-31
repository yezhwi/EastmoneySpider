# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urlparse import urljoin as basejoin
from EastmoneySpider.items import JobboleItem
import datetime


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):

        for post in response.css("#archive .floated-thumb .post-thumb a"):
            img_url = post.css("img::attr(src)").extract_first("")
            post_url = post.css("::attr(href)").extract_first("")
            yield Request(url=basejoin(response.url, post_url), meta={"front_image_url": basejoin(response.url, img_url)},
                          callback=self.parse_detail)


        # 提取下一页并交给scrapy下载
        # next_url = response.css(".next .page-numbers::attr(href)").extract_first("")
        # if next_url:
        #     yield Request(url=next_url, callback=self.parse)


    def parse_detail(self, response):

        jobboleItem = JobboleItem()

        # 文章封面图地址
        front_image_url = response.meta.get("front_image_url", "")
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")

        create_at = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().split()[0]

        # tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tag = ",".join(tag_list)

        praise_nums = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()
        if len(praise_nums) == 0:
            praise_nums = 0
        else:
            praise_nums = int(praise_nums[0])

        fav_nums = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_com = re.match(".*(\d+).*", comment_nums)
        if match_com:
            comment_nums = int(match_com.group(1))
        else:
            comment_nums = 0

        content = response.xpath('//div[@class="entry"]').extract()[0]

        # 这里对地址进行了md5变成定长
        # jobboleItem["url_md5"] = get_md5(response.url)
        jobboleItem["url_md5"] = response.url
        jobboleItem["title"] = title
        jobboleItem["url"] = response.url
        try:
            create_at = datetime.datetime.strptime(create_at, '%Y/%m/%d').date()
        except Exception as e:
            create_at = datetime.datetime.now().date()

        jobboleItem["create_at"] = create_at
        jobboleItem["front_image_url"] = [front_image_url]
        jobboleItem["praise_nums"] = int(praise_nums)
        jobboleItem["fav_nums"] = fav_nums
        jobboleItem["comment_nums"] = comment_nums
        # jobboleItem["tag"] = tag
        jobboleItem['content'] = content

        yield jobboleItem

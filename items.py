# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()dd
    pass


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class JobboleItem(scrapy.Item):
    title = scrapy.Field()
    create_at = scrapy.Field()
    url = scrapy.Field()
    url_md5 = scrapy.Field()
    front_image_url = scrapy.Field()
    # 点赞
    praise_nums = scrapy.Field()
    # 收藏
    fav_nums = scrapy.Field()
    # 评论
    comment_nums = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()

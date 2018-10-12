# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PostItem(scrapy.Item):
    source_url = Field()
    source_name = Field()
    cource_name = Field()
    course_id = Field()
    course_image = Field()
    course_describe = Field()
    course_total_time = Field()
    create_time = Field()
    update_time = Field()
    course_level = Field()
    course_list = Field()
    course_tag = Field()
    is_free = Field()
    course_price = Field()
    course_person = Field()
    course_collect = Field()
    course_like = Field()
    course_evaluate = Field()
    author_name = Field()
    author_id = Field()


class UserItem(scrapy.Item):
    author_name = Field()
    author_id = Field()
    author_image = Field()
    course_author = Field()
    author_platform = Field()
    author_course_list = Field()
    author_course_number = Field()
    author_evaluate = Field()
    author_collect_number = Field()
    author_credit = Field()
    author_evaluate_number = Field()
    author_favorable_rate = Field()

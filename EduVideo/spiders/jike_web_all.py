# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy import Request

home_url = "https://www.jikexueyuan.com/course/"


class JikeSpider(Spider):
    name = "jike_all"

    def start_requests(self):
        self.logger.info("start parse")
        yield Request(url=home_url, callback=self.parse_category_list)

    def parse_category_list(self, response):
        pass

    def parse_list(self, response):
        pass

    def parse_detail(self, response):
        pass

    def parse_user(self, response):
        self.logger.info("parse a person")

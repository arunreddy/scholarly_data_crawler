# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["exapmle.com"]
    start_urls = (
        'http://www.exapmle.com/',
    )

    def parse(self, response):
        pass

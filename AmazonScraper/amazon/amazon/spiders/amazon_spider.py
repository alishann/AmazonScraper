# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2;
    start_urls = [
        'https://www.amazon.com/s?k=gaming+monitors&i=electronics&rh=n%3A1292115011&s=price-asc-rank&dc&qid=1570507024&ref=sr_pg_2'
    ]

    def parse(self, response):
        items = AmazonItem()  # instance of an AmazonItem

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        # product_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        # items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        # next_page = 'https://www.amazon.com/s?k=gaming+monitors&i=electronics&rh=n%3A1292115011&s=price-asc-rank&dc&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1570507024&ref=sr_pg_2'
        # if AmazonSpiderSpider.page_number <= 10:
        #     yield response.follow(next_page, callback=self.parse)
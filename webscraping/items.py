# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TheGuardianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    headline = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    posted_at = scrapy.Field()
    text = scrapy.Field()


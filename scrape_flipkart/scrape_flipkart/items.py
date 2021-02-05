# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    laptop_name = scrapy.Field()
    laptop_reviews = scrapy.Field()
    laptop_ratings = scrapy.Field()
    pass

class DownloadLinksItem(scrapy.Item):
    # define the fields for your item here like:
    links = scrapy.Field()
    pass
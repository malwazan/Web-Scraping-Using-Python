import scrapy
import csv
from ..items import ScrapeReviewsItem
import os
import pandas as pd
# from selenium import webdriver


class ScrapereviewsSpider(scrapy.Spider):
    name = 'ScrapeReviews'

    links = list()
    # create empty csv if not exists
    if not os.path.exists("link.csv"):
        df = pd.DataFrame({"links" : list()})
        df.to_csv("link.csv", index=False, header=False)
    with open('link.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            links.append(row[0])
    links = links[1:]

    start_urls = links

    def __init__(self):
        pass

    def parse(self, response):
        items = ScrapeReviewsItem()

        # find laptop name
        laptop_name = response.css('span.B_NuCI::text').extract()
        if laptop_name is None:
            pass
        else:
            # laptop name
            laptop_name = laptop_name[0]

            reviews = response.css("div.t-ZTKy div div::text").extract()

            ratings = response.css("div._1BLPMq::text").extract()
            
            items['laptop_name'] = laptop_name
            items['laptop_reviews'] = []
            items['laptop_ratings'] = []
            
            for review in reviews:
                items['laptop_reviews'].append(review)
            
            for rating in ratings:
                items['laptop_ratings'].append(rating)
            
            yield(items)
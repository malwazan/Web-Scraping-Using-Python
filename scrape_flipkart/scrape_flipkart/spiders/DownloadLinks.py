import scrapy
from selenium import webdriver
from ..items import DownloadLinksItem

class DownloadLinksSpider(scrapy.Spider):
    name = 'DownloadLinks'
    page_number = 2  # page number for another page to be scraped. It increments itself with every iteration

    start_urls = [
        'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&page=1'
    ]

    def __init__(self):
        #self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        pass

    def parse(self, response):
        # create instance of items
        items = DownloadLinksItem()

        # get all the laptops links
        links = response.css('a._1fQZEK::attr(href)').extract()
        completed_links = ["http://www.flipkart.com" + link for link in links]
        print(completed_links)

        for link in completed_links:
            items['links'] = link
            yield items
        
        next_page = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&page={0}".format(DownloadLinksSpider.page_number)
        if DownloadLinksSpider.page_number <= 29:
            DownloadLinksSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)  # pass parse() method as callback


# for csv with only 1 header line write
#   scrapy crawl <project_name> -o <output_file> -t headless


# Web-Scraping-Using-Python-And-Scrapy

In this Project I used scrapy python to scrape laptop reviews from flipkart.com and store them in json file.

Dependencies Required:
pip install Scrapy
pip install csv
pip install pandas
pip install selenium
----------------------------------------------------------
To run the project:
1.  go to the outer directory where "scrapy.cfg" file is present.
2. Open terminal in that directory
3. type the command:     scrapy crawl DownloadLinks -o links.csv -t headless
    It will download links of all the laptops on flipkart.com
4. now type the following command:     scrapy crawl ScrapeReviews -o output.json
    It will download all the laptops name, reviews, and ratings in to JSON file.
    If you want to download in .csv format then type:    scrape scrapy crawl ScrapeReviews -o output.csv -t headless

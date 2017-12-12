# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:33:42 2017
SCRAPING USING SCRAPY
"""
import scrapy, csv, os


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.onthemarket.com']
    start_urls = ['https://www.onthemarket.com/for-sale/property/london/']


    def parse(self, response):

#        IF FILE RESULT.CSV NOT EXISTS, CREATE IT        
        if not os.path.isfile("result.csv"):
            with open("result.csv", "w", newline = "") as csvfile:
                filewriter = csv.writer(csvfile,  delimiter=",", quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Price", "Number of bedrooms", "Address", "Telephone", "Link"])
        #EXTRACT ALL PRICES
        prices = response.css("a.price::text").extract()
        #EXTRACT NUMBER OF BEDROOMS
        number_of_bedrooms = response.css("span.title a::text").extract()
        #EXTRACT ADDRESS
        address = response.css("span.address a::text").extract()
        #EXTRACT TELEPHONES
        telephone = response.css("strong::text").extract()
        #EXTRACT LINKS TO DESCRIPTION
        link = response.css("span.title a::attr(href)").extract()
        #DELETE SPACES AND NEW LINES IN PRICES
        prices_clean = []
        for price in prices:
            if len((price.replace("\n", "").strip())) > 0:
                prices_clean.append(price.replace("\n", "").strip())

        if os.path.isfile("result.csv"):
            with open(r'result.csv', 'a') as f:
                writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                for index in range(len(prices_clean)):
                    writer.writerow([prices_clean[index],number_of_bedrooms[index],address[index],telephone[index], "www.onthemarket.com" + link[index]])
        #CRAWL ALL PAGINATION TABS            
        next_page_url = response.css("li > a.arrow::attr(href)").extract()[-1]
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
     
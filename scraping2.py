# -*- coding: utf-8 -*-
"""
SCRAPING WEBSITE WITH BeautifulSoup
"""
from bs4 import BeautifulSoup
import requests, time, csv

class scrap(object):
    def __init__(self):
        self.url = "https://www.onthemarket.com/for-sale/property/wigan/"
        self.telephones = []
        self.urls = []
        self.prices = []
        self.num_bedrooms = []
        self.links =[]
        self.address = []
    def extract_page_number(self):
#       REQUEST DATA 
        data = requests.get(self.url, headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(data.text, "lxml")
        count = 0
        for page in soup.findAll("ul", {"class": "pagination-tabs"}):
            for links in page.findAll("a"):
#           ONE NUMBER OF LINK TO PAGE IS NOT AVAILABLE IN SOURCE CODE OF WEBPAGE, SO I CORRECT IT
                if links.get("href")[-1].isdigit():
                    self.urls.append("https://www.onthemarket.com" + links.get("href")[0:-1] + str(count))
                else:
                    self.urls.append("https://www.onthemarket.com" + links.get("href"))
                count += 1
#                   

    def extract_info(self):
        for link in self.urls:
            #SET BEAUTIFULSOUP
            data = requests.get(link, headers={"User-Agent":"Mozilla/5.0"}) # THANKS WWW.STACKOVERFLOW.COM - LEARNED A NEW METHOD
            soup = BeautifulSoup(data.text, "lxml")
            #EXTRACT TELEPHONE NUMBERS
            for tel in soup.findAll("span", {"class":"call"}):
                for exact in tel.findAll("strong"):
                    self.telephones.append(exact.text)
            #EXTRACT PRICES
            for price in soup.findAll("a", {"class":"price"}):
                self.prices.append(price.contents[0].strip())
            #EXTRACT NUMBER OF BEDROOMS AND SAVE LINKS
            for bed in soup.findAll("span", {"class": "title"}):
                for link in bed.findAll("a"):
                    self.links.append("https://www.onthemarket.com" + link.get("href"))
                    self.num_bedrooms.append(link.text.strip())
            #EXTRACT ADDRESS
            for adr in soup.findAll("span", {"class": "address"}):
                for exa in adr.findAll("a"):
                    self.address.append(exa.text.strip())
            #WAIT 1 SECOND BEFORE EXTRACT DATA FROM NEXT PAGE        
            time.sleep(1)
            
    def save(self):
        #CREATE CSV FILE AND ADD DATA
        index = 0
        with open("result.csv", "w", newline = "") as csvfile:
            filewriter = csv.writer(csvfile,  delimiter=",", quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["Price", "Number of bedrooms", "Address ", "Telephone ", "Link"])
            
            while index < len(self.telephones):
                filewriter.writerow([self.prices[index], self.num_bedrooms[index], self.address[index], self.telephones[index], self.links[index]])
                index += 1
#UPDATE VALUES EVERY 24 HOURS        
while True:
    to = scrap()
    to.extract_page_number()
    to.extract_info()
    to.save()
    time.sleep(86400)


# -*- coding: utf-8 -*-
import scrapy, sqlite3, os
from scrapy.selector import Selector
#TO RUN THIS SCRIPT YOU NEED TO INSTALL scrapy
#TO RUN THIS FILE OPEN COMMAND PROMPT
#CD INTO DIRECTORY WHERE IT IS STORED AND TYPE IN scrapy runspider python_sqlite.py

class ScrapySqliteSpider(scrapy.Spider):
    name = 'scrapy_sqlite'
    allowed_domains = ['cphm.ca']
    start_urls = ['http://cphm.ca/company/roster/companyRosterView.html?companyRosterId=5']
    ids = 1
    page_count = 1

    def parse(self, response):
        #CREATE DATABASE IF IT IS NOT ALREADY EXIST
        if not os.path.isfile("pharmacy.db"):
            conn = sqlite3.connect("pharmacy.db")
            conn.execute("""CREATE TABLE PHARMA
                         (ID INT PRIMARY KEY NOT NULL,
                         PHARMACY_LICENSE CHAR(100),
                         STREET CHAR(150),
                         CITY CHAR(30),
                         COUNTRY CHAR(100),
                         LICENSE_HOLDER CHAR(250),
                         MANAGER CHAR(200),
                         TELEPHONE CHAR(100),
                         TELEPHONE_2 CHAR(100),
                         FAX CHAR(100),
                         EMAIL CHAR(250),
                         WEBSITE TEXT,
                         WORKING_HOURS TEXT);""")

        else:
            #CONNECT TO CREATED DATABASE
            conn = sqlite3.connect("pharmacy.db")
        #EXTRACT <td> TAGS that contains needed information    
        licenses = response.css("div#rosterRecords div.col-sm-12 tbody tr td").extract()
        for tag in licenses:
            #EXTRACT TEXT TAG TD   
            td_text = Selector(text=tag).xpath('//td/text()').extract()

            #EXTRACT PHARMACY LICENCE
            if "color" in tag:
                lic = td_text[0].strip()

            #EXTRACT STREET,CITY,COUNTRY, LICENSE HOLDER
            if "font-size: 12px;" in tag and "padding-left" in tag:                
                street = td_text[0].strip()
                city = td_text[1].strip()
                country = td_text[2].strip()
                ph_license_holder = td_text[-1].strip()
                manager = Selector(text=tag).xpath('//span/text()').extract()[0].strip()[18:]

            if "font-size: 12px" in tag and "top" in tag and "50%" not in tag:

                #EXTRACT EMAIL AND LINKS
                emails = Selector(text=tag).xpath('//a/text()').extract()
                #EXTRACT PHONE, FAX
                del_tabs = []
                for item in td_text:
                    del_tabs.append(item.strip())

                phone1 = del_tabs[0]
                phone2 = del_tabs[2]
                fax = del_tabs[4]
#               
                #EXTRACT WORKING HOURS
                if len(del_tabs[-5]) > 0:
                    working_hours = del_tabs[-5][1:].strip()

                #EXTRACT EMAIL AND LINKS
                if len(emails[1]) > 0:
                    website = emails[1].strip()
                if len(emails[0]) > 0:
                    email = emails[0].strip()

                #INSERT VALUES TO DATABASE
                conn.execute("INSERT INTO PHARMA VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.ids, lic, street, city, country, ph_license_holder, manager, phone1, phone2, fax, email, website, working_hours))
                self.ids += 1
        #SAVE AND CLOSE DATABASE        
        conn.commit()
        conn.close()
#       
        #LINKS ARE EXTRACTED WITH JSESSIONID AND THEREFORE NOT WORKING
        #TRAVERSE PAGINATION
        site = response.css("li > a::attr(href)").extract()[-2]
        self.page_count += 1
        next_page_url = "http://cphm.ca/company/roster/companyRosterView.html?companyRosterId=5&page=" + str(self.page_count)
        #href of the last site is #         
        if site != "#":
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
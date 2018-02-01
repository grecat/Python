# -*- coding: utf-8 -*-
import scrapy, psycopg2
from scrapy.selector import Selector

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://www.surf-forecast.com']
    start_urls = ['http://www.surf-forecast.com/breaks/Nusadua/forecasts/latest']

    def parse(self, response):
        try:
            #CONNECT TO DATABASE IF IT EXISTS, USERNAME AND PASSWORD SHOULD BE MODIFIED IF NEEDED
            conn = psycopg2.connect(database ='surf', user='postgres', host='localhost', password='123456')
            conn.autocommit = True
            cur = conn.cursor()
            
        except:
            #CREATE DATABASE IF IT DOES NOT EXISTS AND CONNECT IT, USERNAME AND PASSWORD SHOULD BE MODIFIED IF NEEDED
            conn = psycopg2.connect(user='postgres', host='localhost', password='123456')
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute('CREATE DATABASE surf;')
            cur.close()
            conn.close()
            conn = psycopg2.connect(database ='surf', user='postgres', host='localhost', password='123456')
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("""CREATE TABLE SURF_FORECAST
                         (ID SERIAL NOT NULL PRIMARY KEY,
                         DATE CHAR(50),
                         TIME CHAR(20),
                         RATING CHAR,
                         WAVE_HEIGHT CHAR(20),
                         WAVE_DIRECTION CHAR(10),
                         PERIODS CHAR(20),
                         ENERGY CHAR(20),
                         WIND CHAR(20),
                         WIND_DIRECTION CHAR(10),
                         WIND_STATE CHAR(30),
                         TIDE_STATE CHAR(50),
                         HIGH_TIDE CHAR(30),
                         H_HEIGHT CHAR(20),
                         LOW_TIDE CHAR(30),
                         L_HEIGHT CHAR(20),
                         SUMMARY CHAR(100),
                         RAIN CHAR(20),
                         TEMP CHAR(20),
                         SUNRISE CHAR(10),
                         SUNSET CHAR(10));""")
        
        #EXTRACT ALL DATA
        days = response.css("tr.lar.hea.table-start.weather.secondary_header td b::text").extract()
        data = response.css("tr.lar.hea.table-start.weather.secondary_header td::text").extract()
        time = response.css("tr.hea1.table-end.lar.class_name > td::text").extract()
        tdam = response.css("tr.hea1.table-end.lar.class_name td span::text").extract()
        time_ampm =[]
        datum = []
        for number, ampm in zip(time, tdam):
            time_ampm.append(number.strip() + ampm.strip())
        for day, dat in zip(days, data):
            datum.append(day + dat)
            
        list_data = []
        count = 0
        for tim in time_ampm:
            if tim == "2AM":
                count+=1
            list_data.append(datum[count])
            
        rating = response.css("td.cell img::attr(alt)").extract()
        wave_height = response.css("tr td svg text.swell-icon-val::text").extract()
        all_info = response.css("tr td::text").extract()
        
        wave_direction = all_info[21:39]
        periods = all_info[39:57]
        all_b = response.css("#target-for-range-tabs tr td b::text").extract()
        energy = all_b[3:21]
        
        
        wind_speed = response.css("tr td svg text.wind-icon-val::text").extract()
        wind_direction = all_info[57:75]
        wind_s =response.css("tr:nth-child(9) td b::text").extract()
        wind_state = []
        for ind in range(len(wind_s)):
            if "-" in wind_s[ind]:
                wind_state.append(wind_s[ind] + wind_s[ind + 1])
            if wind_s[ind-1] in ["off", "onshore", "shore", "offshore", "glassy"] and "-" not in wind_s[ind]:
                wind_state.append(wind_s[ind])
        tide_state =all_info[75:93]
        high_tide = response.css("tr.tin.sma td").extract()
        h_tide = []
        h_tide_height =[]
        l_tide = []
        l_tide_height = []
        for link in high_tide:
            td_text = Selector(text=link).xpath('//td/text()').extract()
            ts_text = Selector(text=link).xpath('//td/span/text()').extract()
            if len(h_tide) < 18:
                if len(td_text) == 0:
                    h_tide.append("")
                    h_tide_height.append("")
                else:
                    h_tide.append(td_text[0].strip())
                    h_tide_height.append(ts_text[0].strip())
            else:
                if len(td_text) == 0:
                    l_tide.append("")
                    l_tide_height.append("")
                else:
                    l_tide.append(td_text[0].strip())
                    l_tide_height.append(ts_text[0].strip())
                
        summary = response.css("tr.med.weather.sum td::text").extract()
        rain = response.css("tr.lar.weather td b span::text").extract()
        temperature = response.css("tr.lar.weather td span.temp::text").extract()
        sunrise = all_info[-36:-18]
        sunset = all_info[-18:]

        for index in range(len(sunset)):
            #INSERTING DATA IN POSTGRESQL ONLY IF IT DOESNT ALREADY EXISTS
            cur.execute("""INSERT INTO SURF_FORECAST(
                         DATE,
                         TIME,
                         RATING,
                         WAVE_HEIGHT,
                         WAVE_DIRECTION,
                         PERIODS,
                         ENERGY,
                         WIND,
                         WIND_DIRECTION,
                         WIND_STATE,
                         TIDE_STATE,
                         HIGH_TIDE,
                         H_HEIGHT,
                         LOW_TIDE,
                         L_HEIGHT,
                         SUMMARY,
                         RAIN,
                         TEMP,
                         SUNRISE,
                         SUNSET) SELECT %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s WHERE NOT EXISTS(
                SELECT 1 FROM surf_forecast WHERE date=%s AND time=%s AND energy = %s)""",
            (list_data[index], time_ampm[index], rating[index], wave_height[index],
                wave_direction[index], periods[index], energy[index], wind_speed[index],
                wind_direction[index], wind_state[index], tide_state[index],
                h_tide[index], h_tide_height[index], l_tide[index], l_tide_height[index],
                summary[index].replace("-", ""), rain[index].replace("-", ""), temperature[index], sunrise[index].replace("-", ""), sunset[index].replace("-", ""), list_data[index], time_ampm[index], energy[index]))
        #CLOSE CONNECTION TO DATABASE    
        cur.close()
        conn.close()

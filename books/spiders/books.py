# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class gcdc(scrapy.Spider):
    name = "gcdc_felony"
    start_urls = ['http://publicaccess.co.galveston.tx.us/default.aspx']

    def __init__(self):
        self.driver = webdriver.Firefox()
        def parse(self, response):
            self.driver.get(response.url)
            while True:
                criminal = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/a[3]')
                try:
                    criminal.click()
                    print ("Criminal Click Success")
                    # get the data and write it to scrapy items
                except:
                    break
                    print ("Criminal Click Fail")

    def parse(self, response):
        for test in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

#self.driver.close()

print ("spider ran and finished")

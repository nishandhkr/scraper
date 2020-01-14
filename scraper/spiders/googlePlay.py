import scrapy

class GooglePlay(scrapy.Spider):
    name = "googlePlay"
# seed value must be a valid landing page for a game on google play
    start_urls = [
        "https://play.google.com/store/apps/details?id=com.karuwaapps.loopables"
    ]

# depth limit adjust this value to scrape for longer period
    custom_settings = {
        'DEPTH_LIMIT':20
    }

    def parse(self, response):
        for next_page in response.css('a.JC71ub::attr(href)').getall():
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

             
        yield {'game': response.xpath('//h1[@class = "AHFaub"]/span/text()').get(),
            'totalInstalls': response.xpath('//span[@class="htlgb"]/text()').getall()[2],
            'lastUpdated': response.xpath('//span[@class="htlgb"]/text()').getall()[0],
            'currentVersion': response.xpath('//span[@class="htlgb"]/text()').getall()[3],
            'developer': response.xpath('//span[@class="htlgb"]/text()').getall()[-1],
            'developerAddress': response.xpath('//span[@class = "htlgb"]/div /text()').extract()[-1],
            'developerEmail': response.xpath('//span[@class = "htlgb"]/div/a[starts-with(@href, "mailto:")]/text()').get(),
            #'developerEmail': response.css('a.eUBY6b::text').extract() 
            }


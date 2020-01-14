# scraper
A simple scraper that you can use to get relevant developer information for games on the google play store.

Dependencies: scrapy, python: scrapy is an easy to learn framework that allows us to quickly deploy scrapers. It has full support for
xpath and css and is a great tool to perform artful web-scraping.

I wrote this little script for a friend of mine in game publishing who at the time thought that it could be of some use to him when searching 
for indie developers on the Play Store. 

To use this just run

scrapy crawl googlePlay -o filename.extension

Last time I checked the framework supports JSON, CSV and XML output formats and adjusts automatically to the extension provided.

This scraper as with most scrapers is specific to the Play Store. I use specific css ids and headers to get the information I need.Check the googlePlay.py file in the spiders directory to view the source code, or use it as a template for some other website you want to scrape.

ps. You need to also give the seed URL to the program.  You have to manually do it inside googlePlay.py.

from scrapy.spider import BaseSpider

class DemoSpider(BaseSpider):
    name = "demo"
    allowed_domains = ["localhost"]
    start_urls = [
        "http://localhost:2368/"    
    ]
    
    def parse(self,response):
        print response.body

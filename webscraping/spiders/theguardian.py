import scrapy
from webscraping.items import TheGuardianItem

class TheguardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com']
    start_urls = ['http://theguardian.com/au']

    def parse(self, response):
        # pegando somente as 10 primeiras noticias para evitar block
        for article_link in response.xpath('//a[@data-link-name="article"][@class="fc-item__link"]'):
            url = article_link.xpath('@href').get()
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        item = TheGuardianItem()
        item["url"] = response.url
        item["headline"] = response.xpath('//div[@data-gu-name="headline"]//text()').get()

        item["author"] = response.xpath('//address[@aria-label="Contributor info"]//text()').get()
        item["tags"] = response.xpath('//ul[@class="dcr-1r2wmvc"]/li/a/text()').getall()
        item["text"] = response.xpath('//div[@id="maincontent"]//p//text()').getall()
        item["posted_at"] = response.xpath('//span[@class="dcr-10i63lj"]/text()').get()

        yield item
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://www.qimao5.com/book/957/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//dd')
        links = le.extract_links(response)
        urls = [link.url for link in links]
        name = response.xpath('string(//div[@class="info"]/h1)').extract_first()
        for i in range(50):
            yield scrapy.Request(urls[i], callback=self.getContent, meta={"id": i + 1, "name": name})

    def getContent(self, response):
        book = BookItem()
        book['name'] = response.meta['name']
        book['id'] = response.meta['id']
        book['title'] = response.xpath('string(//h1[@class="wap_none"])').extract_first()
        # book['content'] = response.xpath('//div[@id="chaptercontent"]').extract_first().replace('\u3000', '')
        book['file_urls'] = [response.url]
        # yield book
        return book
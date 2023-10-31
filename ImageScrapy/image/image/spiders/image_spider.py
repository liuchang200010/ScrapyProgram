from scrapy import Spider
import json
from ..items import ImageItem

class ImageSpider(Spider):
    name = 'images'
    start_urls = ['http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000007/vertical?limit=40']

    def parse(self, response):
        json_data = json.loads(response.body)['res']['vertical']
        image = ImageItem()
        image["image_urls"] = [obj['wp'] for obj in json_data]
        yield image



# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BookItem(Item):
    name = Field()
    id = Field()
    title = Field()
    content = Field()

    file_urls = Field()
    files = Field()

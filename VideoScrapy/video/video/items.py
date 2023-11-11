# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class VideoItem(Item):
    file_urls = Field()
    video_id = Field()


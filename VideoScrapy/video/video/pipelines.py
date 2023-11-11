# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from os.path import join
from scrapy.pipelines.files import FilesPipeline


class VideoPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item):
        video_id = item['video_id']
        return join(str(video_id) + ".mp4")



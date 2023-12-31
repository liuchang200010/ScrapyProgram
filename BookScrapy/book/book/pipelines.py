# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pathlib import Path
# import os
from os.path import join
from scrapy.pipelines.files import FilesPipeline

class BookPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     bookName = item['name']
    #     title = item['title']
    #     path = Path(os.getcwd() + "/resources/" + bookName + "/" + str(item['id']) + title + ".html")
    #     file = open(path, 'w', encoding='utf-8')
    #     file.write(item['content'])
    #     file.close()
    #     print(title + " 下载成功")

    def file_path(self, request, response=None, info=None, *, item):
        bookName = item['name']
        title = item['title']
        return join(bookName, str(item['id']) + title + ".html")


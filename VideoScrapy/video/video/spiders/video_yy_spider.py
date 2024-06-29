from scrapy import Spider
import json
from VideoScrapy.video.video.items import VideoItem
from scrapy import cmdline

class ImageSpider(Spider):
    name = 'videos-yy'
    start_urls = ['https://api-tinyvideo-web.yy.com/home/tinyvideosv2']

    def parse(self, response):
        json_data = json.loads(response.body.decode('utf-8'))['data']['data']
        for v in json_data:
            video = VideoItem()
            video['file_urls'] = [v['resurl']]
            video['video_id'] = v['resid']
            yield video

if __name__ == '__main__':
    cmdline.execute('scrapy crawl videos-yy --nolog'.split())

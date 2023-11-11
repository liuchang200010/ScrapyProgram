# ScrapyProgram
使用Scrapy编写爬虫案例

## 0.常用命令

```shell
安装虚拟环境 pip3 install virtualenv
创建虚拟环境 python -m venv venv
激活环境 venv\Scripts\activate (Windows) source venv/bin/activate (Linux)
停用 deactivate
生成requirements.txt pipreqs ./ --encoding utf-8
安装scrapy pip3 install scrapy
scrapy新建项目 scrapy startproject
scrapy启动爬虫 scrapy crawl
```

## 1.爬取文本数据

```python
url: https://www.qimao5.com
使用前需要创建文件资源路径: 例如book/resources/bookName书名
```

## 2.爬取图片数据

```python
url:http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000007/vertical
        
使用scrapy自带的ImagesPipeline无法下载图片，出现以下提示信息，执行 pip3 install pillow
 WARNING: Disabled scrapy.pipelines.images.ImagesPipeline: ImagesPipeline requires installing Pillow 4.0.0 or later
```

## 3.爬取短视频数据

```python
yy直播 url:https://api-tinyvideo-web.yy.com/home/tinyvideosv2
```


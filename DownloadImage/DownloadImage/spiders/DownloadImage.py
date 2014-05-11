from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import os

class DownloadImage(BaseSpider):
    name = "DownloadImage"
    allowed_domains = ["douban.com"]
    download_delay = 0.2
    start_urls = [];
    if not os.path.exists('./Image'):
        os.mkdir('./Image')
    f = open("../GetUrlSpider/ImageUrl.txt",'r')
    line = f.readline()
    while(line):
        start_urls.append(line)
        line = f.readline()
    counter = 0;

    def parse(self, response):
        str = response.url[0:-3];
        self.counter = self.counter+1
        str = str.split('/');
        print '--------------------------------',self.counter,str[-1]
        imgfile = open('./Image/'+str[-1],'wb')
        imgfile.write(response.body)

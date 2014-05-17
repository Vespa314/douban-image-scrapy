from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import os

class GetUrlSpider(BaseSpider):
    name = "downloadspider"
    allowed_domains = ["douban.com"]
    download_delay = 0.2
    counter = 0;
    if not os.path.exists('./Image'):
        os.mkdir('./Image')

    MovieId = [[24532162,11],[21323283,1]]
    start_urls = [];
    for [movie,page] in MovieId:
    	for i in range(0,40*(page+1),40):
        	start_urls.append('http://movie.douban.com/subject/%d/photos?type=S&start=%d&sortby=vote&size=a&subtype=a'%(movie,i))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        req = []
        sites = hxs.select("//ul/li/div[@class='cover']/a/img/@src").extract()
        for site in sites:
            site = site.replace('thumb','raw')
            r = Request(site, callback=self.DownLload)
            req.append(r)
        return req

    def DownLload(self, response):
    	str = response.url[0:-3];
        self.counter = self.counter+1
        str = str.split('/');
        print '----------------Image Get----------------',self.counter,str[-1],'jpg'
        imgfile = open('./Image/'+str[-1]+"jpg",'wb')
        imgfile.write(response.body)

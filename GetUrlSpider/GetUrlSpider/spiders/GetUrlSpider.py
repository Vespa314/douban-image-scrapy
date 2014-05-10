from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class GetUrlSpider(BaseSpider):
    name = "GetUrlSpider"
    allowed_domains = ["douban.com"]
    start_urls = [];
    f = open('ImageUrl.txt', 'wb')

    MovieId = [[24745444,1],[25811384,1]]
    for [movie,page] in MovieId:
    	for i in range(0,40*(page+1),40):
        	start_urls.append('http://movie.douban.com/subject/%d/photos?type=S&start=%d&sortby=vote&size=a&subtype=a'%(movie,i))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//ul/li/div[@class='cover']/a/img/@src").extract()
        for site in sites:
            site = site.replace('thumb','raw')
            #print site
            self.f.write(site)
            self.f.write('\r\n')

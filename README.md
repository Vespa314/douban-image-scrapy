豆瓣相册爬取器
===================


###运行前提：

* python版本为2.7x
* 需要配置好scrapy环境

###配置scrapy环境方法：
请参见[Scrapy抓取豆瓣相册(学习笔记)](http://www.kylen314.com/archives/1529)

###原理：
参见[Scrapy抓取豆瓣相册(学习笔记)](http://www.kylen314.com/archives/1529)

###食用方法：

####1.设置要下载的页面id和页数:
修改`...\douban-image-scrapy\GetUrlSpider\GetUrlSpider\spiders`的`GetUrlSpider.py`,找到`MovieId = [....]`处，这里每个元素是一个`1×2`数组,其中数组第一个元素是电影/动画在豆瓣上的id，第二个元素是该电影/动画相册的页数。

比如想要爬取《反叛的鲁路修》和《钢之炼金术师》的相册，其中鲁鲁修的地址是，[http://movie.douban.com/subject/2043155/](http://movie.douban.com/subject/2043155/),而钢炼的是[http://movie.douban.com/subject/1433342/](http://movie.douban.com/subject/1433342/)，然后再看他们的相册，比如鲁鲁修的[相册](http://movie.douban.com/subject/2043155/photos?type=S)有2页，而钢炼的[相册地址](http://movie.douban.com/subject/1433342/photos?type=S)有4页，所以应该填写的是:
```
MovieId = [[2043155,2],[2043155,4]]
```
修改后保存即可！

####2.获取下载链接

```
cd .\douban-image-scrapy\GetUrlSpider
scrapy crawl GetUrlSpider
```
此时所有的高清图片的URL都将被保存在`...\douban-image-scrapy\GetUrlSpider\ImageUrl.txt`中，可打开查看。

如果数量不多，可以直接投食给迅雷娘服用。

但是如果下载图片数量较多，强烈建议不要使用迅雷，因为很容易出现获取被拒，然后下载失败的情况。

####3.下载图片
```
cd ../DownloadImage
scrapy crawl DownloadImage
```
等运行完毕，即可在`...\douban-image-scrapy\DownloadImage\Image`下找到图片

###后期改进：
有空的话。。。
* 自动检测电影相册页数，只要输入id即可
* 图片按电影分好类
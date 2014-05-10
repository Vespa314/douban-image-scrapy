# Scrapy settings for GetUrlSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'GetUrlSpider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['GetUrlSpider.spiders']
NEWSPIDER_MODULE = 'GetUrlSpider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


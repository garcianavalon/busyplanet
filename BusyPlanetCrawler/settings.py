# Scrapy settings for BusyPlanetCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BusyPlanetCrawler'

SPIDER_MODULES = ['BusyPlanetCrawler.spiders']
NEWSPIDER_MODULE = 'BusyPlanetCrawler.spiders'

ITEM_PIPELINES = {
    'BusyPlanetCrawler.pipelines.RemoveDivTagsPipeline': 400,
    'BusyPlanetCrawler.pipelines.CleanHtmlTagsPipeline': 430,
    'BusyPlanetCrawler.pipelines.RemoveLinksPipeline': 435,
    'BusyPlanetCrawler.pipelines.RemoveLineBreaksPipeline': 440,
    'BusyPlanetCrawler.pipelines.RemoveEmptyStringsPipeline': 450,
    'BusyPlanetCrawler.pipelines.StoringItemInMongoDBPipeline': 900,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BusyPlanetCrawler (+http://www.yourdomain.com)'


# Scrapy settings for BigDataTermProject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BigDataTermProject'

SPIDER_MODULES = ['BigDataTermProject.spiders']
NEWSPIDER_MODULE = 'BigDataTermProject.spiders'

ITEM_PIPELINES = {
    'BigDataTermProject.pipelines.CleanHtmlPTagsPipeline': 400,
    'BigDataTermProject.pipelines.StoringItemInMongoDBPipeline': 900,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BigDataTermProject (+http://www.yourdomain.com)'

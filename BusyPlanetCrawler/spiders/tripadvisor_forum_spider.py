from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spider import Spider

from BusyPlanetCrawler.items import TripAdvisorForumTopicItem,TripAdvisorForumPostItem

class TripAdvisorForumSpider(CrawlSpider):
#class TripAdvisorSpider(Spider):
    name = "tripadvisor_forum"
    allowed_domains = ["tripadvisor.com"]
    f = open("urls/forum_urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    collection_name ="forum"
    rules = (
        #Extract links in the forum topics
        #All forum topic links start with /ShowTopic-
        #we use the provided link extractor with a regexp
        #Callback defines the method to process the Response from the link
        Rule(SgmlLinkExtractor(allow=('ShowTopic', )), callback='parse_item'),
    )

    def parse_item(self, response):
        #self.log('Crawling the link: %s' % response.url)
        sel = Selector(response)
        sel.remove_namespaces()
        topic = sel.xpath("//div[@id='SHOW_TOPIC']")
        item = TripAdvisorForumPostItem()
        item['text'] = topic.xpath("//div[@class='postBody']").extract() #topic.xpath("//p/text()").extract()
        #item['date'] = topic.xpath("//div[@class='postDate']/text()").extract()
        item['link'] = response.url
        return item

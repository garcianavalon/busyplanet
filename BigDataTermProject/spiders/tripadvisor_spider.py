from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spider import Spider

from BigDataTermProject.items import TripAdvisorForumTopicItem,TripAdvisorForumPostItem

class TripAdvisorSpider(CrawlSpider):
#class TripAdvisorSpider(Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = [
        "http://www.tripadvisor.com/ShowForum-g186338-i17-London_England.html",
    ]

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



    '''def parse(self, response):
        sel = Selector(response)
        forum = sel.xpath("//table[@id='SHOW_FORUMS_TABLE']/tr")
        items = []
        for topic in forum:
            item = TripAdvisorForumTopicItem()
            item['title'] = topic.xpath('td/b/a/text()').extract()
            item['link'] = topic.xpath('td/b/a/@href').extract()
            item['replies'] = topic.xpath("td[@class='reply rowentry ']/text()").extract()
            items.append(item)
        return items'''
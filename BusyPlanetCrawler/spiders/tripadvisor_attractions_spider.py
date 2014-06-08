from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spider import Spider
import re
from BusyPlanetCrawler.items import TripAdvisorAttractionReviewItem

class TripAdvisorAttractionsSpider(CrawlSpider):
#class TripAdvisorSpider(Spider):
    name = "tripadvisor_attractions"
    allowed_domains = ["tripadvisor.com"]
    f = open("urls/attractions_urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    collection_name =""
    rules = (
        #Extract links in the forum topics
        #All forum topic links start with /ShowTopic-
        #we use the provided link extractor with a regexp
        #Callback defines the method to process the Response from the link
        Rule(SgmlLinkExtractor(allow=('Attraction_Review', )), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        sel.remove_namespaces()
        reviews = sel.xpath("//div[@class='reviewSelector ']")
        items =[]
        for review in reviews:
            item = TripAdvisorAttractionReviewItem()
            item['text'] = review.xpath("div[@class='review basic_review inlineReviewUpdate provider0 newFlag']/div[@class='col2of2']/div[@class='innerBubble']/div[@class='wrap']/div[@class='entry']/p/text()").extract()
            if not item['text']:
                continue
            score = review.xpath("div[@class='review basic_review inlineReviewUpdate provider0 newFlag']/div[@class='col2of2']/div[@class='innerBubble']/div[@class='wrap']/div[@class='rating reviewItemInline']/span/img/@alt").extract()

            if score:
                regex = re.compile("(\d)")
                r = regex.findall(str(score))#IE: 4 of 5 stars
                item['score'] = float(r[0])#then 4
                item['max_score'] = float(r[1])#then 5

            items.append(item)
        return items
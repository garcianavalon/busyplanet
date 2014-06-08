# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class TripAdvisorForumTopicItem(Item):
    title = Field()
    link = Field()
    replies = Field()

class TripAdvisorForumPostItem(Item):
    text = Field()
    date = Field()
    #destination_mentioned = Field()
    link = Field()
class TripAdvisorAttractionReviewItem(Item):
    text = Field()
    score = Field()
    max_score = Field()

class DummyItem(Item):
    dummy_field = Field()


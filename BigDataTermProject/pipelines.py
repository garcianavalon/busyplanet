# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class StoringItemInMongoDBPipeline(object):
    def process_item(self, item, spider):
        client = MongoClient()
        db = client['bigdata'] #get our database
        collection = db[spider.name] #each spider will store items in its own collection
        collection.insert(dict(item)) #insert in the db
        return item
class CleanHtmlPTagsPipeline(object):
    def process_item(self, item, spider):
        #remove the tags
        new_text = []
        for string in item['text']: #TODO: join both in a regex
            new_text.append(string.replace("<p>","").replace("</p>",""))
        item['text'] = new_text
        return item


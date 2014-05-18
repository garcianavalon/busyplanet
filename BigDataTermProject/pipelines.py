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

class RemoveEmptyStringsPipeline(object):
    def process_item(self, item, spider):
        #remove the empty strings
        new_text = []
        for string in item['text']:
            if string:
                new_text.append(string)
        item['text'] = new_text
        return item

class RemoveLineBreaksPipeline(object):
    def process_item(self, item, spider):
        #remove the tags
        new_text = []
        for string in item['text']:
            new_text.append(string.replace("\n", ""))
        item['text'] = new_text
        return item
import re
class RemoveDivTagsPipeline(object):
    def process_item(self, item, spider):
        #we remove all the useless div tags inside postBody in tripadvisor forum posts
        regex = re.compile('<div.*>', re.IGNORECASE)
        new_text = []
        for string in item['text']:
            no_ending_div_tags_string = string.replace("</div>","")
            new_text.append(regex.sub("",no_ending_div_tags_string))
        item['text'] = new_text
        return item
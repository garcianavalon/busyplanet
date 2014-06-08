# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from pymongo import MongoClient
class StoringItemInMongoDBPipeline(object):
    def process_item(self, item, spider):
        client = MongoClient()
        db = client['bigdata'] #get our database
        collection = db[spider.name + "_paris"] #each spider will store items in its own collection
        collection.insert(dict(item)) #insert in the db
        return item
class CleanHtmlTagsPipeline(object):
    def process_item(self, item, spider):
        #remove the tags
        cleaned_text = []
        for string in item['text']: #TODO: join all in a regex
            cleaned_text.append(string
                .replace("<p>","")
                .replace("</p>","")
                .replace("<small>","")
                .replace("</small>",""))
        item['text'] = cleaned_text
        return item

class RemoveEmptyStringsPipeline(object):
    def process_item(self, item, spider):
        #remove the empty strings
        cleaned_text = []
        for string in item['text']:
            if string:
                cleaned_text.append(string)
        item['text'] = cleaned_text
        return item

class RemoveLineBreaksPipeline(object):
    def process_item(self, item, spider):
        #remove the tags
        cleaned_text = []
        for string in item['text']:
            cleaned_text.append(string.replace("\n", ""))
        item['text'] = cleaned_text
        return item

class RemoveDivTagsPipeline(object):
    def process_item(self, item, spider):
        #we remove all the useless div tags inside postBody in tripadvisor forum posts
        regex = re.compile('<div.*>', re.IGNORECASE)
        cleaned_text = []
        for string in item['text']:
            no_ending_div_tags_string = string.replace("</div>","")
            cleaned_text.append(regex.sub("",no_ending_div_tags_string))
        item['text'] = cleaned_text
        return item

class RemoveLinksPipeline(object):
    def process_item(self, item, spider):
        #we remove all the links in the comments
        regex = re.compile(r'<a [^<]*>[^<]*</a>', re.IGNORECASE)
        cleaned_text = []
        for string in item['text']:
            match = re.findall(regex,string)
            cleaned_string = string
            for link in match:
                cleaned_string = cleaned_string.replace(link,"")
            cleaned_text.append(cleaned_string)
        item['text'] = cleaned_text
        return item

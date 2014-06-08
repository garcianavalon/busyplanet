#lets clean the a tags
from pymongo import MongoClient
import re
client = MongoClient()
db = client['bigdata']

cities = ['london','paris']

regex = re.compile(r'<a [^<]*>[^<]*</a>', re.IGNORECASE)


for city in cities:
    threads_colletion = db['tripadvisor_'+city]
    for thread in threads_colletion.find():
        cleaned_text = []
        for topic in thread["text"]:
            match = re.findall(regex,topic)
            cleaned_topic = topic
            for link in match:
                cleaned_topic = cleaned_topic.replace(link,"")
            cleaned_text.append(cleaned_topic)
        thread['text'] = cleaned_text
        threads_colletion.save(thread)


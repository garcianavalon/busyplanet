f = open('test.txt','r')
sentences = [url.strip() for url in f.readlines()]
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['test']
collection = db['sentences']

for sentece in sentences:
    collection.insert({'text':sentece})
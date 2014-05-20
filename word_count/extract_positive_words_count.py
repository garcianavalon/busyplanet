f = open('positivewords.txt','r')
lines = f.readlines()
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

cities = ['sanfrancisco']
for city in cities:
    for word in lines:
        item = db['word_count_'+city].find({'_id':word})
        db['positive_words_'+city].insert(item)
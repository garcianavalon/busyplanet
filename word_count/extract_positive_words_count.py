f = open('positivewords.txt','r')
lines = [url.strip() for url in f.readlines()]
print lines
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

cities = ['sanfrancisco']
for city in cities:
    all_words = db['word_count_'+city]
    positive_words = db['positive_words_'+city]
    for word in lines:
        item = all_words.find_one({'_id':word})
        if item:
            positive_words.insert(item)
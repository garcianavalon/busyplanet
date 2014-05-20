f = open('negativewords.txt','r')
lines = [url.strip() for url in f.readlines()]
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

cities = ['sanfrancisco','london']
for city in cities:
    print 'Starting with: '+city
    all_words = db['word_count_'+city]
    negative_words = db['negative_words_'+city]
    #clean start
    negative_words.remove()
    for word in lines:
        item = all_words.find_one({'_id':word})
        if item:
            negative_words.insert(item)
    print 'Finished with: '+city
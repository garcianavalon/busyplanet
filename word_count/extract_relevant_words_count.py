f = open('negativewords.txt','r')
negativewords = [url.strip() for url in f.readlines()]
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

cities = ['sanfrancisco','london']
for city in cities:
    print 'Starting with: '+city
    all_words = db['word_count_'+city]
    result_collection = db['result_collection_'+city]
    #clean start
    result_collection.remove()
    for word in negativewords:
        item = all_words.find_one({'_id':word})
        if item:
            result_collection.insert(item)
    print 'Finished with: '+city
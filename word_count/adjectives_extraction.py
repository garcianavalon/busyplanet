f = open('positivewords.txt','r')
adjectives = [url.strip() for url in f.readlines()]
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

def extractWords(index, list):
    words = []
    for i in [index-2,index-1,index,index+1,index+2]:
        if i>0 and i<len(list):
            words.append(list[i])
    return words

cities = ['sanfrancisco','london']
for city in cities:
    print 'Starting with: '+city
    comments_colletion = db['tripadvisor_'+city] #change to the name of your collections
    result_collection = db['result_'+city]
    #clean start
    result_collection.remove()
    for comment in comments_colletion.find().limit(1000):#you can get less for testing
        text = comment['text']
        #add all the text
        text_as_string = ""
        for p in text:
            text_as_string += p.replace(".","").lower()
        text_as_words = text_as_string.split()
        for adjective in adjectives:
            if adjective in text_as_words:
                index = text_as_words.index(adjective)
                words = extractWords(index,text_as_words)
                print(words)
    print 'Finished with: '+city
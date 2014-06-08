import summarize
from pymongo import MongoClient

#SETTINGS
#Number of words
NUMBER_OF_WORDS = 5
#City
CITY = 'sanfrancisco'
#TOPIC
TOPIC = 'beach'
#threads
NUMBER_OF_THREADS = 10000

def getTopics(db,city):
    data = ""
    threads_colletion = db['tripadvisor_'+city]
    for thread in threads_colletion.find().limit(10000):
        for topic in thread["text"]:
            data += topic
    return data

def getWordsByTopics(filename):
    f = open(filename,'r')
    words = [url.strip() for url in f.readlines()]
    f.close()
    return words

def selectMostUsedWords(db,city,words,number_of_words):
    #get the ordered list of words by frequence of appearence
    words_collection = db['word_count_'+city]
    items = words_collection.find({'_id':{ "$in": words }}).sort([("value", -1)]).limit(number_of_words)
    return [item['_id'] for item in items]

def saveToFile(output,filename):
    f = open(filename,'w')
    f.truncate()
    for sentence in output:
        print sentence
        f.write(sentence.encode('utf8')+"\n")
    f.close()

client = MongoClient()
db = client['bigdata']
ss = summarize.SimpleSummarizer()
topic_words = getWordsByTopics(TOPIC+'_words.txt')
# GET FROM DB THE MOST USED ONES
important_words = selectMostUsedWords(db,CITY,topic_words,NUMBER_OF_WORDS)
print important_words
input = getTopics(db,CITY)
output = ss.get_summarized(input, NUMBER_OF_WORDS,important_words)
saveToFile(output,CITY+"_"+TOPIC+".txt")
print "SAVED TO FILE"
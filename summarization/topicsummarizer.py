import summarize
from pymongo import MongoClient

#SETTINGS
#Number of words
NUMBER_OF_WORDS = 10
#City
CITY = 'paris'
#TOPIC
TOPIC = 'art'
#threads
NUMBER_OF_THREADS = 50000

def getTopics(db,city):
    data = []
    threads_colletion = db['tripadvisor_'+city]
    for thread in threads_colletion.find().limit(NUMBER_OF_THREADS):
        text = ""
        for topic in thread["text"]:
            text += topic
        data.append(text)
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

def saveToFile(output_data,filename):
    f = open(filename,'w')
    f.truncate()
    for text in output_data:
        for sentence in text:
            f.write(sentence.encode('utf8')+"\n")
    f.close()

print "summarizing "+CITY +" for "+TOPIC
client = MongoClient()
db = client['bigdata']
ss = summarize.SimpleSummarizer()
topic_words = getWordsByTopics(TOPIC+'_words.txt')
# GET FROM DB THE MOST USED ONES
important_words = selectMostUsedWords(db,CITY,topic_words,NUMBER_OF_WORDS)
print "words: ",important_words
print "fetching input topics..."
input_data = getTopics(db,CITY)
print "Done, starting summarization..."
output_data = []
for thread_text in input_data:
    #print "next chunck..."
    output = ss.get_summarized(thread_text, NUMBER_OF_WORDS,important_words)
    output_data.append(output)
print "Done, saving..."
saveToFile(output_data,CITY+"_"+TOPIC+".txt")
print "Bye!"
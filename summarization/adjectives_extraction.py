f = open('adjectives.txt','r')
adjectives = [url.strip() for url in f.readlines()]
f.close()

from pymongo import MongoClient
client = MongoClient()
db = client['bigdata']

cities = ['sanfrancisco','london']
for city in cities:
    print 'Starting with: '+city
    comments_colletion = db['tripadvisor_'+city] #change to the name of your collections
    result_collection = db['result_'+city]
    #clean start
    result_collection.remove()
    for comment in comments_colletion.find()#you can get less for testing
        #do stuff
        for word in adjectives:
            #do suff
        #save the item in the result collection or print on screen

    print 'Finished with: '+city
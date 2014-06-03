from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers.czech import stem_word
from sumy.utils import get_stop_words

def summarize():
    pass #TODO

def getData(amount=-1):
    from pymongo import MongoClient
    client = MongoClient()
    db = client['bigdata']

    cities = ['sanfrancisco']
    data = []
    for city in cities:
        comments_colletion = db['tripadvisor_'+city]
        for comment in comments_colletion.find().limit(10):
            data.extend(comment['text'])
    return data
if __name__ == "__main__":
    url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    parser = HtmlParser.from_url(url, Tokenizer("czech"))

    summarizer = LsaSummarizer(stem_word)
    summarizer.stop_words = get_stop_words("czech")

    for sentence in summarizer(parser.document, 20):
        #print(sentence)
        pass
    data = getData()
    print(data)


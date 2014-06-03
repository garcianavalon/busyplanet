# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers.czech import stem_word
from sumy.utils import get_stop_words


if __name__ == "__main__":
    url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    parser = HtmlParser.from_url(url, Tokenizer("czech"))

    summarizer = LsaSummarizer(stem_word)
    summarizer.stop_words = get_stop_words("czech")

    for sentence in summarizer(parser.document, 20):
        print(sentence)

def summarize():
    pass #TODO

def getData(amount=-1):
    from pymongo import MongoClient
    client = MongoClient()
    db = client['bigdata']

    cities = ['sanfrancisco']
    data = []
    for city in cities:
        pass
    return data
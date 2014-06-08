# Simple Summarizer
# Copyright (C) 2010-2012 Tristan Havelick
# Author: Tristan Havelick <tristan@havelick.com>
# URL: <https://github.com/thavelick/summarize/>
# For license information, see LICENSE.TXT

"""
A summarizer based on the algorithm found in Classifier4J by Nick Lothan.
In order to summarize a document this algorithm first determines the
frequencies of the words in the document.  It then splits the document
into a series of sentences.  Then it creates a summary by including the
first sentence that includes each of the most frequent words.  Finally
summary's sentences are reordered to reflect that of those in the original
document.
"""

##//////////////////////////////////////////////////////
##  Simple Summarizer
##//////////////////////////////////////////////////////
import nltk.data

class SimpleSummarizer:

	def get_summarized(self, input, num_sentences,important_words):

		# break the input up into sentences.  working_sentences is used
		# for the analysis, but actual_sentences is used in the results
		# so capitalization will be correct.
		print "LOADING sent_detector"
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		print "TOKENIZING"
		actual_sentences = sent_detector.tokenize(input)
		print "BUILDING working_sentences"
		working_sentences = [sentence.lower()
			for sentence in actual_sentences]

		# iterate over the most frequent words, and add the first sentence
		# that inclues each word to the result.
		output_sentences = []
		print "STARTING SEARCH"
		for word in important_words:
			print "searching for "+word
			for i in range(0, len(working_sentences)):
				if (word in working_sentences[i]
				  and actual_sentences[i] not in output_sentences):
					output_sentences.append(actual_sentences[i])
					#break
				#if len(output_sentences) >= num_sentences: break
			#if len(output_sentences) >= num_sentences: break

		return output_sentences

	def summarize_as_text(self, input, num_sentences, important_words):
		return " ".join(self.get_summarized(input, num_sentences, important_words))

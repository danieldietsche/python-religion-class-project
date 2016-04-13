import nltk
from nltk.book import *

#text came from gutenberg project

from nltk.corpus import PlaintextCorpusReader

#This next part makes the four sections of texts corpuses
corpus_root = "."
Matthew = nltk.Text(PlaintextCorpusReader(corpus_root, "Matthew Resurrection.txt").words())
Mark = nltk.Text(PlaintextCorpusReader(corpus_root, "Mark Resurrection.txt").words())
Luke = nltk.Text(PlaintextCorpusReader(corpus_root, "Luke Resurrection.txt").words())
John = nltk.Text(PlaintextCorpusReader(corpus_root, "John Resurrection.txt").words())

search_text.concordance(raw_input(angel),80,27)
import nltk
import os
import sys

#command line argument is the text file name.
input_text = sys.argv[1]

from nltk.corpus import PlaintextCorpusReader

corpus_root = "."
search_text = nltk.Text(PlaintextCorpusReader(corpus_root, input_text).words())

search_text.concordance("angel",200,25)

search_text.concordance("angels",200,25)

search_text.dispersion_plot(["angel","angels"])

from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('bible')
# stopwords in AppData\Roaming\nltk_data\corpora\stopwords
search_text = [word for word in search_text if word.lower() not in stopwords]

fd = nltk.FreqDist(search_text)

print "Number of times used:"
for (key, value) in (fd.items()):
	if key == "angel" or key == "angels":
		print key,value
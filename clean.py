import nltk
import string
from nltk.stem.wordnet import WordNetLemmatizer


def clean_text(total_docs):
	stop = set(nltk.corpus.stopwords.words('english'))
	punc = set(string.punctuation)
	lemma = WordNetLemmatizer()

	result_docs = []
	for doc in total_docs:
		total_words = doc.split()
		stop_free = " ".join([i.lower() for i in total_words if i.lower() not in stop])
		punc_free = ''.join([i for i in stop_free if i not in punc])
		normal = "".join([lemma.lemmatize(i) for i in punc_free])
		result_docs.append(' '+normal+' ')
	return result_docs

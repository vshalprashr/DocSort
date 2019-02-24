import os
from clean import *
from random2 import randint
from collections import Counter

# import numpy as np
# from gensim import corpora

'''num_topics total number of topics
num_words total number of words used
num_docs total number of documents
file_list list of files in directory
path path for input documents
flag used for computing
all_word list of all words used
topic_term_matrix topic to term status
total_docs set of docs retrieved
doc_topic_matrix doc to topic status
doc_term_matrix doc to term frequency'''

path = 'input_docset/'

if __name__ == '__main__':
    num_topics = int(input('Number of topics desired: '))
    file_list = os.listdir(path)
    num_docs = len(file_list)

    # print(file_list)
    # for filename in os.listdir(path):
    #	print('filename: ', filename)
    #	with open(path+filename, 'r') as file:
    #		total_docs.append(file.read())
    total_docs = [
        "This document aims to give an overview of how to contribute to SciPy.  It tries to answer commonly asked questions, and provide some insight into how the community process works in practice.  Readers who are familiar with the SciPy community and are experienced Python coders may want to jump straight to the `git workflow`_ documentation.",
        "On an exceptionally hot evening early in July a young man came out of the garret in which he lodged in S. Place and walked slowly, as though in hesitation, towards K. bridge. He had successfully avoided meeting his landlady on the staircase. His garret was under the roof of a high, five-storied house and was more like a cupboard than a room. The landlady who provided him with garret, dinners, and attendance, lived on the floor below, and every time he went out he was obliged to pass her kitchen, the door of which invariably stood open. And each time he passed, the young man had a sick, frightened feeling, which made him scowl and feel ashamed. He was hopelessly in debt to his landlady, and was afraid of meeting her."]

    print(total_docs)
    cleaned_docs = clean_text(total_docs)
    print(cleaned_docs)

    id2word = {"num_words": -1}
    num_words = -1
    all_word = []
    for doc in cleaned_docs:
        unique_word = Counter(doc.split())
        min_doc = ' '.join(unique_word.keys())
        for word in min_doc.split():
            num_words += 1
            id2word[word] = num_words
            all_word.append(word)

    doc_term_matrix = []
    for doc in cleaned_docs:
        new = []
        for word in all_word:
            new.append(doc.count(' ' + word + ' '))
        doc_term_matrix.append(new)

    topic_term_matrix = []
    for topic in range(num_topics):
        new = []
        for word in all_word:
            new.append(randint(0, 1))
        topic_term_matrix.append(new)

    print(topic_term_matrix)

    doc_topic_matrix = []
    for doc in cleaned_docs:
        new = []
        for topic in range(num_topics):
            flag = 0
            for word in doc.split():
                if topic_term_matrix[topic][id2word[word]] == 1:
                    new.append(1)
                    flag = 1
                    break
            if flag == 0:
                new.append(0)
        doc_topic_matrix.append(new)

    print(doc_topic_matrix)

    '''term_topic_matrix = np.zeros((id_ctr, num_topics))
	print(id_ctr, num_topics)
	for i in range(0, id_ctr):
		for j in range(0, num_topics):
			term_topic_matrix[i, j] = randint(0, 7)
	print(term_topic_matrix)

	for doc in cleaned_docs:
		for word in doc.split():
			freq = [0 for i in range(0,num_topics)]
			for i in range(id2word[word], id2word[word]+6):
				for topic in range(0, num_topics):
					freq[topic] += term_topic_matrix[i][topic]
			term_topic_matrix[id2word[word]] = max(term_topic_matrix[id2word[word]]) + 1
	print(term_topic_matrix)'''

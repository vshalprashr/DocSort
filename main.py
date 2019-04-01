import os
from clean import *
from random2 import randint
from collections import Counter
import numpy as np

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
    num_docs = 2

    print(file_list)
    for filename in os.listdir(path):
    	print('filename: ', filename)
    	with open(path+filename, 'r') as file:
		total_docs.append(file.read())
    '''total_docs = [
        "This document aims to give an overview of how to contribute to SciPy.  It tries to answer commonly asked questions, and provide some insight into how the community process works in practice.  Readers who are familiar with the SciPy community and are experienced Python coders may want to jump straight to the `git workflow`_ documentation.",
        "On an exceptionally hot evening early in July a young man came out of the garret in which he lodged in S. Place and walked slowly, as though in hesitation, towards K. bridge. He had successfully avoided meeting his landlady on the staircase. His garret was under the roof of a high, five-storied house and was more like a cupboard than a room. The landlady who provided him with garret, dinners, and attendance, lived on the floor below, and every time he went out he was obliged to pass her kitchen, the door of which invariably stood open. And each time he passed, the young man had a sick, frightened feeling, which made him scowl and feel ashamed. He was hopelessly in debt to his landlady, and was afraid of meeting her."]
	'''
    print(total_docs)
    cleaned_docs = clean_text(total_docs)
    print(cleaned_docs)

    id2word = {"num_words": -1}
    num_words = -1
    all_word = []
    min_doc = []
    for doc in cleaned_docs:
        unique_word = Counter(doc.split())
        min_doc.append(' '.join(unique_word.keys()))
        for word in doc.split():
            if word not in all_word:
                num_words += 1
                id2word[word] = num_words
                all_word.append(word)

    doc_term_matrix = []
    for doc in cleaned_docs:
        new = []
        for word in all_word:
            new.append(doc.count(' ' + word + ' '))
        doc_term_matrix.append(new)

    topic_term_matrix = np.zeros(shape=(num_topics, len(all_word)), dtype='float')
    total_topic_word = np.zeros(num_topics, dtype='int')
    for word in all_word:
        random_x = randint(0, num_topics-1)
        topic_term_matrix[random_x][id2word[word]] = 1
        total_topic_word[random_x] += 1

    doc_topic_matrix = []
    for doc in cleaned_docs:
        new = []
        for topic in range(num_topics):
            count = 0
            for word in doc.split():
                count += topic_term_matrix[topic][id2word[word]]
            new.append(count / len(doc.split()))
            print(count, len(doc.split()))
            # doc_topic_matrix[iter_doc][topic] = count / len(doc.split())
        # iter_doc += 1
        doc_topic_matrix.append(new)

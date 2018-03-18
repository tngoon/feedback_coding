import csv
import os.path
import string
import codecs
import sys  
import numpy as np
from math import sqrt, log
from itertools import chain, product
from collections import defaultdict

def cosine_sim(u,v):
    return np.dot(u,v) / (sqrt(np.dot(u,u)) * sqrt(np.dot(v,v)))

def generate_vocab(v, list1):
    if v == None:
        return set(list1)
    return set(v+list1)

def vectorize(s, vocab):
    return [s.count(i) for i in vocab]

def corpus2vectors(corpus):
    vectorized_corpus = []
    for i in corpus:
        #print "\n**********************\nYour i is : ", i, "\n*******************************\n"
        vectorized_corpus.append((i, vectorize(i, vocab)))
    return vectorized_corpus, vocab

if __name__ == '__main__':


	input_filename = "data/ixd_w16_feedback.csv"
	
	csv_infile = open(input_filename, 'r')
	output_filename = "data/ixd_w16_feedback_nodups.csv"

	fieldnames = ["ID", "Comment", "Num duplicates"]
	output = []

	reader = csv.DictReader(csv_infile)

	comments = {}
	exclude = set(string.punctuation)
	dont_check_ids = []

	for row in reader:
		ID = row["ID"]
		orig_comment = row["comments"].strip().lower()
		orig_comment = ''.join(ch for ch in orig_comment if ch not in exclude)
		
		comments[ID] = orig_comment
	#print comments

	for comment_id1 in comments:
		if comment_id1 not in dont_check_ids:
			next_row = {"ID": comment_id1, "Comment": comments[comment_id1], "Num duplicates": 0}

			for comment_id2 in comments:
				if comment_id1 != comment_id2:                
					vocab1 = comments[comment_id1].split()
					vocab2 = comments[comment_id2].split()
					vocab = set(vocab1 + vocab2)
					all_data = [vocab1, vocab2]
					corpus, vocab = corpus2vectors(all_data)

					i = 1
					j = 1
					#print corpus[0][0]
					#print corpus[1][0]

					cosine = cosine_sim(corpus[0][1], corpus[1][1])
					if cosine > 0.65:
						print "THESE COMMENTS ARE SIMILAR"
						print corpus[0][0]
						print corpus[1][0]
						print cosine
						print "\n\n"
						next_row["Num duplicates"] = next_row["Num duplicates"] + 1
						dont_check_ids.append(comment_id2)
			output.append(next_row)

	csv_outfile = open(output_filename, 'w')

	writer = csv.DictWriter(csv_outfile, fieldnames=fieldnames)

	writer.writeheader()
	writer.writerows(output)


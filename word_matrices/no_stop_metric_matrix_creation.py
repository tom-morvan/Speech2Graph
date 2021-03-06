#metric matrix creation
import numpy as np
from nltk.corpus import stopwords

word_list = np.load("../word_lists/word_list.npy")
word_matrix = np.load("../word_matrices/word_matrix.npy")
metric_list_fr = np.load("../word_lists/metric_list_fr.npy")
metric_matrix = np.zeros((len(metric_list_fr),300))
stop = set(stopwords.words('french'))

index = 0
for metric in metric_list_fr:
	except_1 = False
	words = [i for i in metric.lower().split() if i not in stop]
	print(words)
	metric_vector = [0 for i in range(300)]

	for word in words :
		if word[:2] == "d'" or word[:2] == "l'":
			word = word[2:]
		if word == "reception":
			word = "réception"
		try :
			word_index = int(np.where(word_list == word)[0])
			metric_vector += word_matrix[word_index]
		except :
			except_1 = True 
		if except_1 == True :	
			try :
				word_index = int(np.where(word_list == word)[0][0])
				metric_vector += word_matrix[word_index]
			except :
				print("{} is not in word_matrix".format(word))
	metric_matrix[index] = metric_vector
	index += 1

np.save("no_stop_metric_matrix", metric_matrix)
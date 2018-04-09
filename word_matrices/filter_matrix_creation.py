#filter matrix creation
import numpy as np

word_list = np.load("../word_lists/word_list.npy")
word_matrix = np.load("../word_matrices/word_matrix.npy")
filter_list_fr = np.load("../word_lists/filter_list_fr.npy")
filter_matrix = np.zeros((len(filter_list_fr),300))
index = 0
for filter in filter_list_fr:
	except_1 = False
	words = filter.split()
	filter_vector = [0 for i in range(300)]

	for word in words :
		if word[:2] == "d'" or word[:2] == "l'":
			word = word[2:]
		if word == "reception":
			word = "réception"
		try :
			word_index = int(np.where(word_list == word)[0])
			filter_vector += word_matrix[word_index]
		except :
			except_1 = True 
		if except_1 == True :	
			try :
				word_index = int(np.where(word_list == word)[0][0])
				filter_vector += word_matrix[word_index]
			except :
				print("{} is not in word_matrix".format(word))
	filter_matrix[index] = filter_vector
	index += 1

np.save("filter_matrix", filter_matrix)
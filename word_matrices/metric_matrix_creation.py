#metric matrix creation

word_list = np.load("word_list")
word_matrix = np.load("word_matrix")
metric_list_fr = np.load(metric_list_fr)
metric_matrix = np.zeros((len(metric_list_fr),300))
index = 0
for metric in metric_list_fr:
	words = sentence.split()
	metric_vector = [0 for i in range(300)]

	for word in words :
		try :
			word_index = int(np.where(word_list == word)[0])
			metric_vector += word_matrix[word_index]
		except :
			print("{} is not in word_matrix".format(word))
	metric_matrix[index] = metric_vector
	index += 1

np.save("metric_matrix")
#filter matrix creation

word_list = np.load("word_list")
word_matrix = np.load("word_matrix")
filter_list_fr = np.load(filter_list_fr)
filter_matrix = np.zeros((len(filter_list_fr),300))
index = 0
for filter in filter_list_fr:
	words = sentence.split()
	filter_vector = [0 for i in range(300)]

	for word in words :
		try :
			word_index = int(np.where(word_list == word)[0])
			filter_vector += word_matrix[word_index]
		except :
			print("{} is not in word_matrix".format(word))
	filter_matrix[index] = filter_vector
	index += 1

np.save("filter_matrix")
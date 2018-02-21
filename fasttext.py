import numpy as np
# from gensim.models import KeyedVectors


# word_matrix = np.zeros((50000,300))
# word_list = []
# parsed_section_matrix = np.zeros((1,300))

# word_matrix creation

# with open("wiki.fr.vec") as f:
# 	i = 2
# 	f.readline()

# 	for line in f:
# 		if i <= 50001 :
# 			values = line.split()
# 			word = values[0]

# 			coefs = np.zeros((1,300))
# 			l = [i for i in range(0,len(values)-1)]
# 			try :
# 				coefs[0,l] = values[1:]
# 			except :
# 				index = 1
# 				test_float = ['0.']
# 				for el in values[1:]:
# 					try :
# 						test_float = float(el)
# 					except:
# 						values[index] = '0.'
# 					index += 1
# 				continue
# 			word_list.append(word)
# 			word_matrix[i-2,:] = coefs
# 			i+=1

# np.save('word_matrix', word_matrix)
# np.save('word_list', word_list)
word_list = np.load('word_list.npy')
word_matrix = np.load('word_matrix.npy')
dimension_matrix = np.load('dimension_matrix.npy')
dimension_list_fr = np.load('dimension_list_fr.npy')
sentence = "nom de l'endroit"
words = sentence.split()
sentence_vector = [0 for i in range(300)]

for word in words :
	except_1 = False
	if word[:2] == "d'" or word[:2] == "l'":
			word = word[2:]
	try :
		word_index = int(np.where(word_list == word)[0])
		sentence_vector += word_matrix[word_index]
	except :
		except_1 = True 
	if except_1 == True :	
		try :
			word_index = int(np.where(word_list == word)[0][0])
			sentence_vector += word_matrix[word_index]
		except :
			print("{} is not in word_matrix".format(word))

result_vector = [0 for i in range(len(dimension_list_fr))]
index = 0

for line in dimension_matrix :
	somme = 0
	for el in line :
		somme += el**2
	result_vector[index] = line.dot(sentence_vector)/np.sqrt(somme)
	index += 1
minimum_indexes = np.zeros((1,1))

for index in range(1):
	min_index = result_vector.index(max(result_vector))
	minimum_indexes[index] = min_index
	result_vector[min_index] = 10000

closest_dimensions = []
for index in minimum_indexes:
	closest_dimensions.append(dimension_list_fr[int(index)])

print(closest_dimensions)
	






# dot_product_matrix = word_matrix.dot(np.transpose(parsed_section_matrix))



# jp_model = KeyedVectors.load_word2vec_format('wiki.ja.vec')

# jp_model.most_similar('car')




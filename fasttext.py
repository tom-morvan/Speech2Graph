import numpy as np
# from gensim.models import KeyedVectors

Sentence = ""

word_matrix = np.zeros((50000,300))
word_list = []
parsed_section_matrix = np.zeros((1,300))

# word_matrix creation

with open("wiki.fr.vec") as f:
	i = 2
	f.readline()

	for line in f:
		if i <= 50001 :
			values = line.split()
			word = values[0]

			coefs = np.zeros((1,300))
			l = [i for i in range(0,len(values)-1)]
			try :
				coefs[0,l] = values[1:]
			except :
				index = 1
				test_float = ['0.']
				for el in values[1:]:
					try :
						test_float = float(el)
					except:
						values[index] = '0.'
					index += 1
				continue
			word_list.append(word)
			word_matrix[i-2,:] = coefs
			i+=1

word = 'voiture'
word_index = word_list.index('voiture')



# print(word_list)

result_vector = [0 for i in range(50000)]
index = 0
for line in word_matrix:
	somme = 0 
	for el in line - word_matrix[word_index] :
		somme += el**2
	result_vector[index] = np.sqrt(somme)
print(result_vector)

# dot_product_matrix = word_matrix.dot(np.transpose(parsed_section_matrix))



# jp_model = KeyedVectors.load_word2vec_format('wiki.ja.vec')

# jp_model.most_similar('car')




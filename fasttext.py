import fasttext
import numpy as np
# from gensim.models import KeyedVectors

Sentence = ""

word_matrix = np.zeros((50000,300))
word_list = []
parsed_section_matrix = np.zeros((1,300))

# word_matrix creation

with open("../../Downloads/wiki.fr.vec") as f:
	i = 2
	f.readline()

	for line in f:
		if i <= 5 :
			values = line.split()
			word = values[0]

			coefs = np.asarray(values[1:], dtype='float32')
			word_list.append(word)
			print(np.shape(coefs))
			print(np.shape(word_matrix))
			# word_matrix[i-2,:] = coefs

			i+=1


# dot_product_matrix = word_matrix.dot(np.transpose(parsed_section_matrix))



# jp_model = KeyedVectors.load_word2vec_format('wiki.ja.vec')

# jp_model.most_similar('car')




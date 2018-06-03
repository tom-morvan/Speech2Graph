import numpy as np
from scipy import spatial

word_list = np.load('/.../word_lists/word_list.npy')
word_matrix = np.load('/.../word_matrices/word_matrix.npy')

def getWordVector(word):
    except_1 = False
    if word[:2] == "d'" or word[:2] == "l'":
        word = word[2:]
    try:
        return word_matrix[int(np.where(word_list == word)[0])]
    except BaseException:
        except_1 = True
    if except_1:
        try:
            return word_matrix[int(np.where(word_list == word)[0][0])]
        except BaseException:
            print("{} is not in word_matrix".format(word))

def getClosestWords(word, amount):
	"""Returns the "amount" closest words to the input word"""
	word_vector = getWordVector(word)
	closest_words = []
	closest_word_vectors = []
	results_vector = []
	for line in word_matrix:
		results_vector.append(spatial.distance.cosine(line, word_vector))
	for _ in range(amount):
		min_index = results_vector.index(min(results_vector))
		closest_word_vectors.append(results_vector[min_index])
		results_vector[min_index] = 10000  
		closest_words.append(word_list[min_index])


	return closest_word_vectors

print(getClosestWords("maire", 10))

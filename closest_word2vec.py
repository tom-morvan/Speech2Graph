import numpy as np
from scipy import spatial

word_list = np.load('word_lists/word_list.npy')
word_matrix = np.load('word_matrices/word_matrix.npy')
dimension_matrix = np.load('word_matrices/dimension_matrix.npy')
dimension_list_fr = np.load('word_lists/dimension_list_fr.npy')
metric_matrix = np.load('word_matrices/metric_matrix.npy')
metric_list_fr = np.load('word_lists/metric_list_fr.npy')
filter_matrix = np.load('word_matrices/filter_matrix.npy')
filter_list_fr = np.load('word_lists/filter_list_fr.npy')

def getWordVector(word):
   except_1 = False
   if word[:2] == "d'" or word[:2] == "l'":
       word = word[2:]
   try :
       return word_matrix[int(np.where(word_list == word)[0])]
   except :
       except_1 = True 
   if except_1 == True :   
       try :
           return word_matrix[int(np.where(word_list == word)[0][0])]
       except :
           print("{} is not in word_matrix".format(word))

def getEuclideanDistances(sentence_vector, vector_matrix):
   # Euclidean distance
   result_vector = []
   for line in vector_matrix :
       result_vector.append(spatial.distance.euclidean(line, sentence_vector))
   return result_vector

def getBraycurtisDistances(sentence_vector, vector_matrix):
   # BrayCurtis distance
   result_vector = []
   for line in vector_matrix :
       result_vector.append(spatial.distance.braycurtis(line, sentence_vector))
   return result_vector

def getCosineDistances(sentence_vector, vector_matrix):
   # Cosine distance
   result_vector = []
   for line in vector_matrix :
       result_vector.append(spatial.distance.cosine(line, sentence_vector))
   return result_vector

def getMinkowskiDistances(sentence_vector, vector_matrix, p):
   # Minkowski distance
   result_vector = []
   for line in vector_matrix :
       result_vector.append(spatial.distance.minkowski(line, sentence_vector, p))
   return result_vector

def getClosest(results_vector, thing_list_fr):
   min_index = results_vector.index(min(results_vector))
   results_vector[min_index] = 10000 #what's this for Owain?
   return thing_list_fr[min_index]



def closestFilters(pre_ontology_filter, amount):
   words = pre_ontology_filter.split()
   sentence_vector = [0 for i in range(300)]    # vector representation of the input sentence (initialisation)

   for word in words :
       sentence_vector = sentence_vector + getWordVector(word) # You forgot to sum them
   
   results_vector = getCosineDistances(sentence_vector, filter_matrix)  # contains the vector distance between the sentence vector and each filter vector

   closest_filters = []
   for _ in range(amount):
       closest_filters.append(getClosest(results_vector, filter_list_fr))  # get the "amount" closest

   return closest_filters

def closestDimensions(pre_ontology_dimension, amount):
   words = pre_ontology_dimension.split()
   sentence_vector = [0 for i in range(300)]    # vector representation of the input sentence (initialisation)

   for word in words :
       sentence_vector = sentence_vector + getWordVector(word)
   
   results_vector = getCosineDistances(sentence_vector, dimension_matrix)  # contains the vector distance between the sentence vector and each dimension vector

   closest_dimensions = []
   for _ in range(amount):
       closest_dimensions.append(getClosest(results_vector, dimension_list_fr))  # get the "amount" closest

   return closest_dimensions

def closestMetrics(pre_ontology_metric, amount):
   words = pre_ontology_metric.split()
   sentence_vector = [0 for i in range(300)]    # vector representation of the input sentence (initialisation)

   for word in words :
       sentence_vector = sentence_vector + getWordVector(word)
   
   results_vector = getCosineDistances(sentence_vector, metric_matrix)  # contains the vector distance between the sentence vector and each metris vector

   closest_metrics = []
   for _ in range(amount):
       closest_metrics.append(getClosest(results_vector, metric_list_fr))  # get the "amount" closest

   return closest_metrics

print(closestMetrics("salaire net", 3))

def closestAgregation(pre_ontology_agregation, amount):
   words = pre_ontology_agregation.split()
   sentence_vector = [0 for i in range(300)]    # vector representation of the input sentence (initialisation)

   for word in words :
       sentence_vector = sentence_vector + getWordVector(word)
   
   results_vector = getCosineDistances(sentence_vector, agregation_matrix)  # contains the vector distance between the sentence vector and each agregation vector

   closest_agregation = []
   for _ in range(amount):
       closest_metrics.append(getClosest(results_vector, metric_list_fr))  # get the "amount" closest

   return closest_agregation
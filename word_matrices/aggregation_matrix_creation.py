#aggregation matrix creation
import numpy as np

word_list = np.load("../word_lists/word_list.npy")
word_matrix = np.load("../word_matrices/word_matrix.npy")
aggregation_list_fr = np.array(['somme','moyenne','nombre'])
aggregation_matrix = np.zeros((len(aggregation_list_fr),300))

index = 0
for aggregation in aggregation_list_fr:
    except_1 = False
    words = aggregation.split()
    metric_vector = [0 for i in range(300)]

    for word in words :
        if word[:2] == "d'" or word[:2] == "l'":
            word = word[2:]
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
    aggregation_matrix[index] = metric_vector
    index += 1

np.save("aggregation_matrix", aggregation_matrix)

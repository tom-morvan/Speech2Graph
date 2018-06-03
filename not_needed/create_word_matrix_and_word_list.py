# creates word_matrix and word_list for 50000 words

import numpy as np
word_matrix = np.zeros((50000,300))
word_list = []
parsed_section_matrix = np.zeros((1,300))

#word_matrix creation

with open("wiki.fr.vec") as f:
    i = 2
    f.readline()

    for line in f:
        if i <= 50001 :
            values = line.split()
            word = values[0]

            coefs = np.zeros((1,300))
            l = [j for j in range(0,len(values)-1)]
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

np.save('word_matrix', word_matrix)
np.save('word_list', word_list)
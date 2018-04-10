
import speech_recognition as sr
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
import numpy as np

# TODO: Turn the following section of code into a function, with loops, etc.
# def get_speech()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something!")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language='fr-FR')
    print(text)
except:
    text = "Nom de l'endroit"
    # for testing
    # text = None
    print("Sorry, I didn't understand that.")
    pass

# initilazation of gensim word embedding
fr_model = KeyedVectors.load_word2vec_format('wiki.fr/wiki.fr.vec')

tolkenized_text = word_tokenize(text, language='french')
print(tolkenized_text)

# TODO: French-POS tagging

#TODO: clearer varuiable names
word_list = np.load('word_lists/word_list.npy')
word_matrix = np.load('word_matrices/word_matrix.npy')
# dimension_matrix = np.load('word_matrices/dimension_matrix.npy')
# dimension_list_fr = np.load('word_lists/dimension_list_fr.npy')

sentence_vector = [0 for i in range(300)]
filtered_words = []

#primary filtration algorithm
for word in tolkenized_text:
    except_1 = False
    if word[:2] == "d'" or word[:2] == "l'":
            word = word[2:]
    if word in fr_model:
        filtered_words.append(word)
    else:
        print("{} is not in word_matrix".format(word))

print(filtered_words)

#getting synonyms for words
for word in filtered_words:
    your_word_vector = fr_model.get_vector(word)
    synonyms = fr_model.most_similar(positive=[your_word_vector], topn=5)
    print(synonyms)

#TODO: find most similar words to those in filtrations, dimensions, etc

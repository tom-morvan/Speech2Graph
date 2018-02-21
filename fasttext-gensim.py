
import speech_recognition as sr
from gensim.models import KeyedVectors
import nltk


#def get_speech():

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say Something!')
    audio = r.listen(source)
try:
    print(r.recognize_google(audio, language='fr-FR')) #fr-FR
except:
    pass


# text = get_speech()
# print(text)

fr_model = KeyedVectors.load_word2vec_format('src/wiki.fr.vec')

# # # Getting the tokens
# # words = []
# # for word in fr_model.vocab:
# #     words.append(word)

# # Pick a word
find_similar_to = "voiture"

# Finding out similar words [default= top 10]
for similar_word in fr_model.similar_by_word(find_similar_to):
    print("Word: {0}, Similarity: {1:.2f}".format(
        similar_word[0], similar_word[1]
    ))

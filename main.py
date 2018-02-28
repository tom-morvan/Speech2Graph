import speech_recognition as sr
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
import numpy as np

import polyglot
from polyglot.text import Text, Word
from polyglot.downloader import downloader

# Correspondances :
# ADJ: adjective
# ADP: adposition
# ADV: adverb
# AUX: auxiliary verb
# CONJ: coordinating conjunction
# DET: determiner
# INTJ: interjection
# NOUN: noun
# NUM: numeral
# PART: particle
# PRON: pronoun
# PROPN: proper noun
# PUNCT: punctuation
# SCONJ: subordinating conjunction
# SYM: symbol
# VERB: verb
# X: other

def parser(text):
    """Parses the text into sub groups of words
    Returns a list of the subgroups"""
    agregation = []
    metric = []
    dimension= [[]]
    filters = [[]]

    text = Text(text, hint_language_code='fr')
    pos_tags = text.pos_tags


    # Finding the agregation
    verb_counter = 0
    noun = None
    i = 0

    while noun == None and i < len(pos_tags):

        if pos_tags[i][1] == 'VERB':
            verb_counter += 1

        if verb_counter > 0:

            if pos_tags[i][1] == 'NOUN':
                noun = pos_tags[i][0]
                agregation_pos = i

        i += 1

    agregation.append(noun)

    # Finding the metric
    i = agregation_pos + 1

    while i < len(pos_tags) and pos_tags[i][1] != 'ADP':

        metric.append(pos_tags[i][0])
        i += 1

    end_metric_pos = i - 1

    # Finding the dimensions
    i = end_metric_pos + 1
    dimension_counter = 0

    while i < len(pos_tags) and pos_tags[i][1] != 'CONJ':
        print(pos_tags[i][1])

        if pos_tags[i][0] == 'et':
            dimension_counter += 1
            dimension.append([])

        else:
            dimension[dimension_counter].append(pos_tags[i][0])

        i += 1

    end_dimension_pos = i - 1

    # Finding the filters
    i = end_dimension_pos + 1
    filter_counter = 0

    while i < len(pos_tags):

        if pos_tags[i][0] == 'et':
            filter_counter += 1
            filters.append([])

        else:
            filters[filter_counter].append(pos_tags[i][0])

        i += 1

    return([agregation, metric, dimension, filters])

def main():
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

    [agregation, metric, dimension, filters] = parser(tolkenized_text)
    print(agregation)
    print(metric)
    print(dimension)
    print(filters)

if __name__ == "__main__":
    main()

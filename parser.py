
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:10:01 2017

@author: tom
"""

import polyglot
from polyglot.text import Text, Word
from polyglot.downloader import downloader

#print(downloader.supported_languages_table("pos2"))



#Correspondances : 
#ADJ: adjective
#ADP: adposition
#ADV: adverb
#AUX: auxiliary verb
#CONJ: coordinating conjunction
#DET: determiner
#INTJ: interjection
#NOUN: noun
#NUM: numeral
#PART: particle
#PRON: pronoun
#PROPN: proper noun
#PUNCT: punctuation
#SCONJ: subordinating conjunction
#SYM: symbol
#VERB: verb
#X: other



blob = """Je veux la moyenne d'âge des agents en fonction de leur salaire."""
#blob2 = """ Quel est la moyenne d'âge des personnes travaillant en mairie et qui gagnent plus 3000 par mois?"""
#text = Text(blob, hint_language_code='fr')
#print(text.pos_tags)


def text_parser(text):
    """Parses the text into sub groups of words
    Returns a list of the subgroups"""
    agregation = []
    metric = []
    dimension= [[]]
    filters = [[]]
    
    text = Text(text, hint_language_code='fr')
    pos_tags = text.pos_tags
    
    
    #Finding the agregation
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
    
    #Finding the metric    
    i = agregation_pos + 1
    
    while i < len(pos_tags) and pos_tags[i][1] != 'ADP':
        
        metric.append(pos_tags[i][0])
        i += 1
    
    end_metric_pos = i - 1
    
    #Finding the dimensions
    i = end_metric_pos + 1
    dimension_counter = 0

    while i < len(pos_tags) and pos_tags[i][1] != 'CONJ':
        print(pos_tags[i][1])
        
        if pos_tags[i][0] == 'et':
            dimension_counter += 1
            dimension.append([])
        
        else :
            dimension[dimension_counter].append(pos_tags[i][0])
        
        i += 1
        
    end_dimension_pos = i-1
    
    #Finding the filters
    i = end_dimension_pos + 1
    filter_counter = 0
    
    while i < len(pos_tags) :
        
        if pos_tags[i][0] == 'et':
            filter_counter += 1
            filters.append([])
        
        else :
            filters[filter_counter].append(pos_tags[i][0])
        
        i += 1
        
    return([agregation,metric,dimension,filters])    
    
    




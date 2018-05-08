# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:44:47 2018

@author: THINKPAD TT470
"""



import nltk 
nltk.download('averaged_perceptron_tagger')

from nltk.tag import StanfordPOSTagger
jar = 'C:/Users/THINKPAD TT470/Desktop/stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = 'C:/Users/THINKPAD TT470/Desktop/stanford-postagger-full-2018-02-27/models/french.tagger'
import os
java_path = "C:/Program Files/Java/jdk1.8.0_121/bin/java.exe"
os.environ['JAVAHOME'] = java_path

def det_or_nb(string):
    if string.isdigit():
            return 'nb'
    else:
        if len(string)>3:
            return 'nb'
        else:
            if string=='six' or string=='dix':
                return 'nb'
            else:
                return 'det'

def proper_noun(sentence):
    tagged_sentence = nltk.tag.pos_tag(sentence.split())
    proper_noun = [word for word,tag in tagged_sentence if tag == 'NNP' or tag == 'NNPS']
    del(proper_noun[0])
    return(' '.join(proper_noun))

def number(sentence):
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
    tagged_sentence= pos_tagger.tag(sentence.split())
    numbers = [word for word,tag in tagged_sentence if tag == 'DET' and det_or_nb(word)=='nb']
    return(' '.join(numbers))
    
def token_before(token, sentence):
    k=0
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
    tagged_sentence= pos_tagger.tag(sentence.split())
    for i in range(len(tagged_sentence)):
        if tagged_sentence[i][0]==token:
            k=i
    if tagged_sentence[k-1][1]=='P' and tagged_sentence[k-2][1]=='ADJ':
        l=[tagged_sentence[k-2][0],tagged_sentence[k-1][0]]
        return(' '.join(l))
    else:
        return None

def token_after(token, sentence):    
    k=0
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
    tagged_sentence= pos_tagger.tag(sentence.split())
    for i in range(len(tagged_sentence)):
        if tagged_sentence[i][0]==token:
            k=i
    if tagged_sentence[k+1][1]=='NC':
        return(' '.join([tagged_sentence[k+1][0]]))
    else:
        return None    
            

def filter_value(sentence):
    proper=proper_noun(sentence)
    num=number(sentence)
    if proper != '':
        return proper
    else:
        if num != '':
            if token_before(num, sentence) == None:
                return num
            else:
                if token_after(num, sentence) == None:
                    return token_before(num, sentence)+' '+ num
                else:
                    return token_before(num, sentence)+' '+ num+' ' +token_after(num, sentence)
        else:
            return 0 #token after the filter
        
    
s0='Je veux le nombre d’absences des agents avec un temps de travail supérieur à 7 heures en fonctions de l’âge des agents. '            
s1='Donnez-moi le nombre de la paie mensuelle sous le nom de l’entité Madame Bovina.'
s3='Je veux les absences avec le nombre de jour d’absences supérieur à trois semaines en fonction de la nature d’absence.'
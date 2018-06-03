# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:44:47 2018

@author: THINKPAD TT470
"""



import nltk
from nltk.tag import StanfordPOSTagger

jar = '/Users/owainbiddulph/Documents/GitHub/stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = '/Users/owainbiddulph/Documents/GitHub/stanford-postagger-full-2018-02-27/models/french.tagger'
import os
java_path = "/Library/Java/JavaVirtualMachines/jdk1.8.0_161.jdk/Contents/Home/bin/java.exe"
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
    proper_noun = [word for word,tag in tagged_sentence if (tag == 'NNP' or tag == 'NNPS') and word != 'à']
    try:
        del(proper_noun[0])
    except:
        pass
    return(' '.join(proper_noun))

def number(sentence):
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
    tagged_sentence= pos_tagger.tag(sentence.split())
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = [word for word,tag in tagged_sentence if ((tag == 'DET' and det_or_nb(word) == 'nb') or (word[0] in int_list))]
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
    if sentence[-1] == ".":
        sentence = sentence[:-1]
    proper=proper_noun(sentence)
    num=number(sentence)
    if proper != '':
        return proper
    else:
        if num != '':
            if token_before(num, sentence) == None:
                return num
            else:
                try :
                    if token_after(num, sentence) == None:
                        return token_before(num, sentence)+' '+ num
                    else:
                        return token_before(num, sentence)+' '+ num+' ' +token_after(num, sentence)
                except :
                    return num
        else:
            return None #token after the filter
        
    
s0="Je veux le nombre d'absences des agents avec un temps de travail supérieur à 7 heures en fonctions de l’âge des agents."         
s1="Donnez-moi le nombre de la paie mensuelle sous le nom de l’entité Monsieur Dupont."
s2 = "Donnez-moi le nombre d'absences par nature d’absence pour les agents dont le nombre de jour d’absences est supérieur à trois semaines."
s3="Je veux la moyenne d'âge des agents en fonction du sexe des agents dont la date de début du poste est inférieur à 2010."
s4="Donnez-moi la le nombre d'absences par nature d'absence pour les agents dont le nombre de jour d’absences étant supérieur à trois semaines."
s5 = "Donnez-moi la somme des absences en fonction du nombre d’heure d’absences avec le nom de l’entité Monsieur Dupont."
# print(filter_value(s0))
# print(filter_value(s1))
# print(filter_value(s2))
# print(filter_value(s3))
# print(filter_value(s4))
# print(filter_value(s5))
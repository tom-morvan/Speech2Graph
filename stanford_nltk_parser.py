# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:25:50 2018

@author: tom
"""

import os
from nltk.parse import stanford

os.environ['CLASSPATH'] = '/Users/owainbiddulph/Documents/GitHub/stanford-parser-full-2018-02-27'
os.environ['STANFORD_MODEL'] = '/Users/owainbiddulph/Documents/GitHub/stanford-parser-full-2018-02-27'
parser = stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/frenchFactored.ser.gz")


def tree_parser(tree,node_list):
    """Reursive function which take in argument a tree and a list. The function adds to the list the nodes that are
    at the same depth iif they are final leaves. If not, it does the same thing on the sub tree"""
    
    same_depth_node_list = []
    
    for i in range (0,len(tree)): #Looking for the nodes that are located at the same depth and that are leaves
        
        if len(tree[i]) == 1:
            same_depth_node_list.append(tree[i])
            
    node_list.append(same_depth_node_list) #Addind those nodes to the node_list
    
    for i in range (0,len(tree)): #Iteration on the sub-trees
        
        if len(tree[i]) >= 2:
            tree_parser(tree[i],node_list)
            
def tree_parser_flat(tree,node_list):
    same_depth_node_list = []
    
    for i in range (0,len(tree)): #Looking for the nodes that are located at the same depth and that are leaves
        
        if len(tree[i].leaves()) == 1:
            same_depth_node_list.append(tree[i].leaves()[0])
            
    node_list.append(same_depth_node_list) #Addind those nodes to the node_list
    
    for i in range (0,len(tree)): #Iteration on the sub-trees
        
        if len(tree[i].leaves()) >= 2:
            tree_parser_flat(tree[i],node_list)

def parsing(sentence):
    """Takes in argument a sentence (string) and returns a list of the semantic bits of the sentence"""
        
    for line in parser.raw_parse(sentence): #parsing our sentence into a tree
        tree = line[0]
    
    print(tree.pretty_print()) #Showing the Tree
    
    node_list = []
    
    tree_parser(tree,node_list)
    
    return(node_list)
    

def parsing_flat(sentence):
    """Takes in argument a sentence (string) and returns a list of the semantic bits of the sentence"""
        
    for line in parser.raw_parse(sentence): #parsing our sentence into a tree
        tree = line[0]
    
    print(tree.pretty_print()) #Showing the Tree
    
    node_list = []
    
    tree_parser_flat(tree,node_list)
    
    return(node_list)

def seperation_1(sentence):
    """Takes in argument a sentence (string) and returns the presumed ontology"""
    
    parsed_sentence = parsing(sentence)
    
    divided_sentence = [[]]
    divided_leaves = [[]]
    number_of_chunks = 0
    
    for chunk in parsed_sentence:
        
        print(chunk)        
        
        if len(chunk) == 1:
            
            if chunk[0].label() in ['P','PROREL']:
                number_of_chunks += 1
                divided_sentence.append([])
                divided_leaves.append([])
                
            else:
                divided_sentence[number_of_chunks].append(chunk)
                for tree in chunk:
                    divided_leaves[number_of_chunks].append(tree.leaves())
                
        else:
            divided_sentence[number_of_chunks].append(chunk)
            for tree in chunk:
                    divided_leaves[number_of_chunks].append(tree.leaves())
    
       
    return(divided_sentence, divided_leaves)
        
        
def seperation_2(sentence):
    """ splits the sentence into subgroups based on their function in the sentence"""
    
    for line in parser.raw_parse(sentence): #parsing our sentence into a tree
        tree = line[0]
    
    print(tree.pretty_print())    
    
    divided_sentence = []
    divided_leaves = []
    
    for sub_tree in tree:
        
        divided_sentence.append(sub_tree)
        
        divided_leaves.append(sub_tree.leaves())
    
        
    
    return(divided_sentence, divided_leaves)


# def grammatical_seperation(sentence):
#     """ splits the sentence into subgroups based on their function in the sentence"""
    
#     for line in parser.raw_parse(sentence): #parsing our sentence into a tree
#         tree = line[0]
    
#     #print(tree.pretty_print())    
    
#     VN = []
#     NP = []
#     PP = []
#     VN_leaves=[]
#     NP_leaves=[]
#     PP_leaves=[]
#     rest = []
#     rest_leaves = []    
    
#     for sub_tree in tree:
        
#         if sub_tree.label() == 'VN':
#             VN.append(sub_tree)
#             VN_leaves.append(sub_tree.leaves())
#         elif sub_tree.label() == 'NP':
#             NP.append(sub_tree)
#             NP_leaves.append(sub_tree.leaves())
#         elif sub_tree.label() == 'PP':
#             PP.append(sub_tree)
#             PP_leaves.append(sub_tree.leaves())
#         else:
#             if sub_tree.label() != 'PUNC':
#                 rest.append(sub_tree)
#                 rest_leaves.append(sub_tree.leaves())
        
#     return(NP_leaves,VN_leaves,PP_leaves,rest_leaves)
    
def grammatical_seperation(sentence):
    """ splits the sentence into subgroups based on their function in the sentence"""
    
    for line in parser.raw_parse(sentence): #parsing our sentence into a tree
        tree = line[0]
    
    # print(tree.pretty_print())    
    
    VN = []
    NP = []
    PP = []
    VN_leaves=[]
    NP_leaves=[]
    PP_leaves=[]
    rest = []
    rest_leaves = []    

    for sub_tree in tree:
        
        if sub_tree.label() == 'VPinf':
            for sub_sub_tree in sub_tree:            
                if sub_sub_tree.label() == 'VN':
                    VN.append(sub_sub_tree)
                    VN_leaves.append(sub_sub_tree.leaves())
                elif sub_sub_tree.label() == 'NP':
                    NP.append(sub_sub_tree)
                    NP_leaves.append(sub_sub_tree.leaves())
                elif sub_sub_tree.label() == 'PP':
                    PP.append(sub_sub_tree)
                    PP_leaves.append(sub_sub_tree.leaves())
                else:
                    if sub_sub_tree.label() != 'PUNC':
                        rest.append(sub_sub_tree)
                        rest_leaves.append(sub_sub_tree.leaves())
        
        elif sub_tree.label() == 'VN':
            VN.append(sub_tree)
            VN_leaves.append(sub_tree.leaves())
        elif sub_tree.label() == 'NP':
            NP.append(sub_tree)
            NP_leaves.append(sub_tree.leaves())
        elif sub_tree.label() == 'PP':
            PP.append(sub_tree)
            PP_leaves.append(sub_tree.leaves())
        else:
            if sub_tree.label() != 'PUNC':
                rest.append(sub_tree)
                rest_leaves.append(sub_tree.leaves())
        
    return(NP_leaves,VN_leaves,PP_leaves,rest_leaves)
    
def parse_to_pre_ontology(sentence):
    
    seperated_sentence = grammatical_seperation(sentence)
    
    NP = seperated_sentence[0]
    VN = seperated_sentence[1]
    PP = seperated_sentence[2]    
    rest = seperated_sentence[3]
    
    aggregation = []
    metric = []
    dimension= []
    filters = []    
    
    if len(rest) != 0:
        aggregation.append(rest[0]) #change the type
        
    else: #aggregation in NP
        for sub_NP in reversed(NP):
            
            if len(sub_NP) > 1:
                
                if "moyenne" in sub_NP or "moyen" in sub_NP:
                    aggregation = ["moyenne"]
                    try:                    
                        sub_NP.remove("moyenne")
                    except:
                        sub_NP.remove("moyen")
                    metric = sub_NP
                elif "somme" in sub_NP:
                    aggregation = ["somme"]
                    sub_NP.remove("somme")
                    metric = sub_NP 
                else:
                    aggregation = ["nombre"]
                    metric = sub_NP
     
    
    for sub_PP in PP:
        if "fonction" in sub_PP:
            sub_PP.remove("fonction")
            dimension.append(sub_PP)
        elif "par" in sub_PP :
            sub_PP.remove("par")
            dimension.append(sub_PP)
        else:
            filters.append(sub_PP)
    
    return([aggregation,metric,dimension,filters])
    
    
        
def strip(list_of_lists):
    
    L = []    
    
    for element in list_of_lists:
        if len(element) >= 2:
            L.append(element)
    
    return L

#print(parse_to_pre_ontology("Quel est la moyenne d'age des agents en fonction de leur sexe"))


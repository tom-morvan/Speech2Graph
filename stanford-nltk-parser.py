# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:25:50 2018

@author: tom
"""

import os
from nltk.parse import stanford

os.environ['CLASSPATH'] = '/home/tom/Bureau/stanford-parser-full-2018-02-27'
os.environ['STANFORD_MODEL'] = '/home/tom/Bureau/stanford-parser-full-2018-02-27'
parser = stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/frenchFactored.ser.gz")


### Understanding the nltk.tree.Tree class

#sentences = parser.raw_parse("Quel est la moyenne d'age des personnes?")
#print (sentences)
##print(sentences[0]) -> doesn't work type list iterator
#print(type(sentences))
#for line in sentences:
#    #print(line.pretty_print())
#    print("line:", line, "type(line):", type(line))
#    print("line[0]:", line[0], "type(line[0]", type(line[0]))  #line[0] is the same as sentence in line
#    for sentence in line:
#        print("sentence:", sentence)
#        """for t in sentence.subtrees():
#            print(t)"""
##        sentence.draw()

### Defining our chunker


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
        
        if len(tree[i]) == 1:
            same_depth_node_list.append(tree[i].leaves()[0])
            
    node_list.append(same_depth_node_list) #Addind those nodes to the node_list
    
    for i in range (0,len(tree)): #Iteration on the sub-trees
        
        if len(tree[i]) >= 2:
            tree_parser_flat(tree[i],node_list)

def parsing(sentence):
    """Takes in argument a sentence (string) and returns a list of the semantic bits of the sentence"""
        
    for line in parser.raw_parse(sentence): #parsing our sentence into a tree
        tree = line[0]
    
    print(tree.pretty_print()) #Showing the Tree
    
    node_list = []
    
    tree_parser_flat(tree,node_list)
    
    return(node_list)
    

    
    

'''GUI
for line in sentences:
    for sentence in line:
        sentence.draw()'''


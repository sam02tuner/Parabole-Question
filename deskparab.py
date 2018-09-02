# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 16:10:15 2018

@author: suman
"""

import logging
import os
import nltk
from nltk.corpus import wordnet

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def create_knowledge_graph(contents_of_input_file, name_of_input_file):
    
    sentence=contents_of_input_file.split("\n")
    tags=[]
    
    #For tokenizing and finding the nouns, pronouns etc.
    for sen in sentence:
        tokens = nltk.word_tokenize(sen)
        tagged = nltk.pos_tag(tokens)
        tags.append(tagged)

    sptag=[]

    #For separating out the proper noun, singular noun and the noun
    for i in range(len(tags)):
        for j in range(len(tags[i])):
            if(tags[i][j][1]=="NNS" or tags[i][j][1]=="NNP" or tags[i][j][1]=="NN"):
                sptag.append(tags[i][j][0])

    #For removing the duplicates from the list
    newsptag=[]
    for word in sptag:
        word=word.capitalize()
        if(word.endswith("s")):
            word=word[:-1]
        
        newsptag.append(word)

    
    final_list = []
    for num in newsptag:
        if num not in final_list:
            final_list.append(num)

    print(final_list)
    print("\n")
    
    
    pass

#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "C:/Users/suman/Desktop/ParaboleSelectionsPy3/data/input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:29:07 2019
@author: Ezat Elzalouy
"""

import re
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db=myclient['GPdatabase']
words_model = db["Words"]
choose_model=db["choose"]

# Reading Activities
class Models():
    def __init__(self,level):
        self.level=level
        self.words=Models.Reading_Words(self)
        self.choose_words=Models.Choose_Words(self)
        self.choose_hearning_sentences=Models.Choose_Hearning_Sentences(self)
        self.word_index=0
        self.choose_word_index=0
        self.choose_hearning_sentences_index=0

    def Reading_Words(self):
        return words_model.find({"level":self.level})
    def Choose_Words(self):
        return choose_model.find({"level":self.level,"choose_type":"words"})
    def Choose_Hearning_Sentences(self):
        return choose_model.find({'level':self.level,"choose_type":"hearing sentence choose"})
    def Insert_Word(self,name,path,description,examples):
        row={
         "word":name,
         "image":path,
         "Description":description,
         "Examples":examples,
         "level":self.level
         }
        words_model.insert_one(row)
    def Insert_Choose(self,question,correct_choose,wrong_chooses,choose_type):
        row={
                "question":question,
                "correct_choose":correct_choose,
                "wrong_chooses":wrong_chooses,
                "level":self.level,
                "choose_type":choose_type
                }
        choose_model.insert(row)
    def Next(self):
        question=None
        answer=None
        state=None
        if self.word_index<self.words.count():
            message=self.words[self.word_index]
            question={'word':message['word'],'description':message['Description'],'image':message['image'],'examples':message['Examples']}  
            answer=["done","explain"]
            state={'state':1,'activity':'reading','sub-activity':'reading words'}
            self.word_index+=1

        elif self.choose_word_index<self.choose_words.count():
            message=self.choose_words[self.choose_word_index]
            self.choose_word_index+=1
            question={'question':message['question'],'correct_choose':message['correct_choose'],'wrong_chooses':message['wrong_chooses']}
            answer=[message['correct_choose']]
            state={'state':1,'activity':'reading','sub-activity':'choose words'}

        elif self.choose_hearning_sentences_index<self.choose_hearning_sentences.count():
            message=self.choose_hearning_sentences[self.choose_hearning_sentences_index]
            self.choose_hearning_sentences_index+=1
            question={'question':message['question'],'correct_choose':message['correct_choose'],'wrong_chooses':message['wrong_chooses']}
            answer=[message['correct_choose']]
            state={'state':1,'activity':'hearing','sub-activity':'hearing sentence choose'}
        else:
            question=None
            answer=None
            state={'state':0,'activity':'writing','sub-activity':''}
        return question,answer,state

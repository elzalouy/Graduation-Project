# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:29:07 2019

@author: Ezat Elzalouy
"""

import re
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["AssistantDB"]
words_model = db["Words"]
choose_words_model=db["choose_words"]
# Reading Activities
class Reading_Model():
    def __init__(self,level):
        self.level=level
        Reading_Model.Reading_Words(self)
        Reading_Model.Choose_Words(self)
        self.word_index=0
        self.choose_word_index=0
    
    
    def Reading_Words(self):
        self.words=choose_words_model.find({},{"level":self.level})
    def Choose_Words(self):
        self.choose_words=choose_words_model.find({},{"level":self.level})
    def Insert_Word(self,name,path,description,examples,level):
        row={
         "word":name,
         "image":path,
         "Description":description,
         "Examples":examples,
         "level":level
         }
        words_model.insert_one(row)
    def Insert_Choose_Words(self,question,correct_choose,wrong_chooses,level):
        row={
                "question":question,
                "correct_choose":correct_choose,
                "wrong_chooses":wrong_chooses,
                "level":level
                }
        choose_words_model.insert(row)      
    def Next(self):
        question=None
        answer=None
        state=None
        if self.word_index!=self.words.count:
            message=self.words[self.word_index]
            self.word_index+=1
            state={state:1,'activity':'reading','sub-activity':'reading words'}
            question={'word':message['word'],'description':message['Description'],'image':message['image'],'examples':message['Examples']}
            answer=["Done","Explain?"]
            
        elif self.choose_word_index!=self.choose_words.count:
            message=self.choose_words[self.choose_word_index]
            self.choose_word_index+=1
            state={state:1,'activity':'reading','sub-activity':'choose words'}
            question={'question':message['question'],'correct_choose':message['correct_choose'],'wrong_chooses':message['wrong_chooses']}
            answer=[message['correct_choose']]
        else:
            question=None
            answer=None
            state={'state':0,'activity':'writing','sub-activity':''}
        return question,answer,state
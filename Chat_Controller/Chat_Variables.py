# -*- coding: utf-8 -*-
"""
Created on Fri May  3 01:00:55 2019

@author: Ezat Elzalouy
"""

bot_name="English Assistant"
User_Public_messages={
        "Let's See the account":
        [
                "account",
                "Let's see the account",
                "I want to see the account",
                "see the account",
                "profile",
                "let's see the profile",
                "i want to see the account",
                "i want to see my score"
                ],
        "what's that":
        [
                "",
                "what is your purpose",
                "what's your name",
                "what is your name",
                "what is this service",
                "who are you",
                "what is that"
                ],
        "start laerning":
        [
                "let's start",
                "start learning",
                "let's start learning",
                "could we start learning",
                "i need to acquire a knowledge of english",
                "i hope to memorise a big quantity of words",
                "will you instruct me and teach me ?",
                "you will teach me more about english",
                "i want to discover more good things in english",
                "i will find out how to learn english by help of you",
                "you will get me lines of english",
                "will you get me any word ?",
                "hope to hear from you good pronounce",
                "you will learn me how to pick up any sentence and understand it",
                "you will see me how to speak english",
                "i will ascertain of my language, alright",
                "i can check my language skills here, right",
                "i need to determine my skills",
                "I came to acquire a powerful tongue and ear in English",
                "my target is to read more about english",
                "need to improve the reading skills",
                "surely need to study all the aspects of english",
                "take a journey around English aspects."
                ],
        "meaning of":
        [
                "what is the mean of",
                "what is",
                "what is meant by",
                "i need to know the meaning of",
                ],
        "learn words":
        [
                "I need to lean some words",
                "Know some words",
                "save words in memory",
                "learn words"
                ]
        }
Chat_public_messages={
        "What's your name":
        [
                "My name is {0}".format(bot_name)+". ",
                "They call me {0}".format(bot_name)+". " ,
                "It's {0}".format(bot_name)+". ",
                "You can call me {0}".format(bot_name)+". ",
                ],
        "what is your purpose":
        [
                "I can teach you many different skills in english",
                "I am here to take a journey around english skills",
                "I will help improve your english tongue and grammar",
                "My job is to teach you how to use english"
                ],
        "start learning":
                [
                        "let's start learning",
                "Ok, We will help you  to learn more about english",
                "The skills you need to improve are reading, writing, speaking, and listening. Let's start",
                "Sure, Let's Go",
                "We will start now!"
                ],
        "Let's See the account":[
                "Sure, I will see you your account info right now",
                "Ok, I will display your account info right now"
                ],
        "learn word":[
                "I will help you to learn some words in english. let's start",
                "OK, Let's learn some words",
                "that's a good start, learning words is a good step. Let's learn"
                ],
        ""
        "default":"Sorry I don't understand what do you need"
}

Chat_Requests_Responses={
        "start learning?":["I hope you like that, and let's start learning. okay?",
                           "Can we satrt now?"],
        "start learning.":{"yes":["sure","okay","yes","of course","let's start"], "no":["no","sorry","don't like","bad"]},
        "reading words?":
            [
                    "I will show you some words to learn now, okay?",
                    "Here are some words to make english more powerfull",
                    "some words first!",
                    "firstly, learn some words"
                    ],
            "reading words":{
                    "yes":
                    ["sure","okay","yes","of course","let's start"]
                    ,"no":
                    ["sorry","no","don't like","bad","not now"]
                    },
                "no.":
                ["i hope you like that. how can i help ?","if you don't like that, so how can i help you?"],
                "wrong answer.":["Sorry, that's not the answer.","Ooh, i will help you.","that's wrong, let me help you."]            
        }

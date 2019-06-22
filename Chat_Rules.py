import random
import   DB_Models.Models as DBmodels
import json
class Chat:
    def __init__(self):
        self.messages={'message':[],'image':'','audio':''}
        self.user_message=''
        self.Current_State={'state':0,'activity':'','sub-activity':''}
        self.Profile_history={'username':'','email':'','level':0,'marks':{'0':0,'1':0,'2':0,'3':0,'4':0}}
        self.question=[]
        self.answer=[]
        self.Models=DBmodels.Models(self.Profile_history['level'])

    #check if the chat has a response for the message
    def Messages_Rules(self):
        with open('Chat_Variables.json') as env:
            env=json.load(env)
            # what can the chat do ? (messages)
            if self.user_message in env['User_Public_messages']["what can you do"]:
                self.messages['message'].append(random.choice(env["Chat_public_messages"]["the services"]))
                self.Current_State={'state':0,'activity':'','sub-activity':''}
            # start learning
            elif self.user_message in env["User_Public_messages"]["start laerning"]:
                self.messages['message'].append(random.choice(env['Chat_public_messages']["let's start learning"]))
                self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}

            #what's that
            elif self.user_message in  env["User_Public_messages"]["what's that"]:
                self.messages['message'].append(random.choice(env["Chat_public_messages"]["What's your name"])+random.choice(env["Chat_public_messages"]["what is your purpose"]))

            #let's see the account
            elif self.user_message in env["User_Public_messages"]["let's see the account"]:
                self.messages['message'].append(random.choice(env["Chat_public_messages"]["Let's See the account"]))

            # let's learn some words
            elif self.user_message in env["User_Public_messages"]['learn words']:
                self.messages['message'].append(random.choice(env["Chat_public_messages"]["learn words"]))
                self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}

    #check all  the user rules.
    def User_Rules(self):
        if self.Current_State['state']==1:
            self.EvaluateAnswer()
        elif self.Current_State['activity']!='':
            self.NextActivity()
    # Reponse to the user
    def respond(self,message):
        self.user_message=message
        self.messages={'message':[],'image':'','audio':''}
        self.Messages_Rules()
        self.User_Rules()
        return self.messages

    def EvaluateAnswer(self):
        with open('Chat_Variables.json') as env:
            env=json.load(env)

            if self.question != [] and self.answer != []:
                    if self.Current_State['activity']=='reading':
                        # reading words evaluation
                        if self.Current_State['sub-activity']=='reading words':
                            if self.user_message in env['Chat_public_messages']['done']:
                                self.Profile_history['marks'][str(self.Profile_history['level'])]+=1
                                self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}
                                self.messages['message'].append(random.choice(env['Chat_public_messages']["correct answer"]))
                                self.NextActivity()
                                #save the value to the user data here

                            elif self.user_message in env["Chat_public_messages"]["explain"]:
                                self.messages['message'].append('here are an example')
                                self.messages['message'].append(random.choice(self.question['examples']))
                                self.Current_State={'state':1,'activity':'reading','sub-activity':'reading words'}

                        #choose words evaluation
                        elif self.Current_State['sub-activity']=='choose words':
                            if  self.user_message in self.answer:
                                self.Current_State['state']=0
                                self.Profile_history['marks'][str(self.Profile_history['level'])]+=1
                                self.messages['message'].append(random.choice(env['Chat_public_messages']['correct answer']))
                                self.NextActivity()
                            else:
                                with open('Chat_Variables.json') as env:
                                    self.messages['message'].append(random.choice(env['Chat_public_messages']['wrong answer.']))
                                    self.messages['message'].append(random.choice(env['Chat_public_messages']['the answer is: ']))
                                    self.messages['message'].append(self.answer)

                    elif self.Current_State['activity']=="hearing":
                        if self.Current_State['sub-activity']=='hearing sentence choose':
                            if self.user_message.lower() == self.answer[0].lower():
                                self.messages['message'].append(random.choice(env['Chat_public_messages']['correct answer']))
                                self.NextActivity()
                            else:
                                self.messages['message'].append(random.choice(env['Chat_public_messages']['wrong answer.']))

    def NextActivity(self):
        self.question,self.answer,self.Current_State=self.Models.Next()
        if self.Current_State['activity']=='reading':
            if self.Current_State['sub-activity']=='reading words':
                self.messages['message'].append(self.question['word'])
                self.messages['message'].append(self.question['description'])
                self.messages['image']=self.question['image']
            elif self.Current_State['sub-activity']=='choose words':
                chooses=self.question['wrong_chooses']
                chooses.append(self.answer)
                random.shuffle(chooses)
                self.messages['message'].append([self.question['question'],chooses])
        elif self.Current_State['activity']=='hearing':
            if self.Current_State['sub-activity']=='hearing sentence choose':
                self.messages['message'].append(['choose the right sentence that you heard'])
                chooses=self.question['wrong_chooses']
                chooses.append( self.answer)
                random.shuffle(chooses)
                self.messages['message'].append(chooses)

#test chat rules.
chat=Chat()
print(chat.respond("what can you do"))
print(chat.respond("let's start learning"))
print(chat.respond('explain it'))
print(chat.respond("done"))
print(chat.respond("okay"))
print(chat.respond("understand"))
print(chat.respond('file:///home/ezat-elzalouy/Projects/Graduation%20Project/Solution/Images/animals/baboon.jpg'))
print(chat.respond('I like eating at this resturant'))
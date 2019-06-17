import random
import Models as DBmodels
import json
class Chat:
    def __init__(self):
        self.messages=[]
        self.user_message=''
        self.Current_State={'state':0,'activity':'','sub-activity':''}
        self.Profile_history={'username':'','email':'','level':0,'marks':{'0':0,'1':0,'2':0,'3':0,'4':0}}
        self.question=[]
        self.answer=[]
        self.Reading_Model=DBmodels.Reading_Model(self.Profile_history['level'])

    #check if the chat has a response for the message
    def Messages_Rules(self):
        with open('Chat_Variables.json') as env:
            env=json.load(env)
            if self.user_message in env["User_Public_messages"]["start laerning"]:
                self.messages.append(random.choice(env["Chat_public_messages"]["let's start learning"]))
                self.Current_State={'state':1,'activity':'reading','sub-activity':'reading words'}
            elif self.user_message in env["User_Public_messages"]["let's see the account"]:
                self.messages.append(random.choice(env["Chat_public_messages"]["Let's See the account"]))
                self.Current_State={'state':0,'activity':'','sub-activity':0}
            elif self.user_message in env["User_Public_messages"]['learn words']:
                self.messages.append(random.choice(env["Chat_public_messages"]["learn words"]))
                self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}
            elif self.user_message in  env["User_Public_messages"]["what's that"]:
                self.messages.append(random.choice(env["Chat_public_messages"]["What's your name"])+random.choice(env["Chat_public_messages"]["what is your purpose"]))

    #check all  the user rules.
    def User_Rules(self,message):
        if self.Current_State['state']==1:
            self.EvaluateAnswer()
        elif self.Current_State['state']==0:
            self.Activities_Rules()


    # Reponse to the user
    def respond(self,message):
        self.user_message=message
        self.messages=[]
        self.Messages_Rules()
        self.User_Rules(message)
        return self.messages




    def EvaluateAnswer(self):
        if self.question != None and self.answer != None:
                if self.Current_State['activity']=='reading':
                    if self.Current_State['sub-activitiy']=='reading words':
                        if self.user_message.contains(self.answer[0]):
                            self.Current_State['state']=0
                            self.Profile_history['marks']['0']+=1
                            self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}
                        else:
                            self.messages=''




    def Activities_Rules(self):
        # if reading activity
        if self.Current_State['activity']=='reading':
            self.question,self.answer,self.Current_State=self.Reading_Model.Next()
            if self.Current_State['sub-activity']=='reading words':
                self.messages=[self.question['word'],self.question['description'],self.question['image']]
            elif self.Current_State['sub-activity']=='choose words':
                chooses=[self.question['correct_choose'],self.question['wrong_chooses']]
                random.shuffle(chooses)
                self.messages=[self.question['question'],chooses]


chat=Chat()
message=chat.respond("what's that")
print(message)

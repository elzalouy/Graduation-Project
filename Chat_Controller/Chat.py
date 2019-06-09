#!/solution/Models
import random
import Chat_Variables  as env
from Models import Reading_Model as reading_model
from Models import Writing_Model as writing_model
class Chat:
    def __init__(self):
        self.message=[]
        self.Current_State={'state':0,'activity':'','sub-activity':''}
        self.Profile_history={'username':'','email':'','level':0,'marks':{'0':0,'1':0,'2':0,'3':0,'4':0}}
        self.question=[]
        self.answer=[]
        self.Reading_Model=reading_model.Reading_Model(self.Profile_history['level'])
        self.Writing_Model=writing_model.Writing_Model(self.Profile_history['level'])
        
    def respond(self,message):
        # if the state of the chat is zero then it is not waiting a reponse from the user else then the chat is waiting a respo
        if self.Current_State["state"]==0:
            Chat.Chat_State_Zero(self,message)
        else:
            Chat.Chat_State_One(self,message)
        return self.message
            
    def Chat_State_Zero(self,message):
            # if the message refers to that the user needs to start learning
            if message in env.User_Public_Requests['start laerning']:
                self.message.append(random.choice(env.Chat_public_responses["let's start learning"]))
                self.question,self.answer,self.Current_State=self.Reading_Model.Next()
                self.message=[self.question['word'],self.question['description'],self.question['image']]
            #If the user is asking about the chat
            elif message in env.User_Public_Requests["what's that"]:
                self.message=random.choice(env.Chat_public_responses["What's your name"])+ random.choice(env.Chat_public_responses["what is your purpose"])
            # if the user is in reading state
            elif self.Current_State['activtiy']=='reading':
                self.question,self.answer,self.Current_State=self.Reading_Model.Next()
                if self.Current_State['sub-activity']=='reading words':
                    self.message=[self.question['word'],self.question['description'],self.question['image']]
                elif self.Current_State['sub-activity']=='choose words':
                    chooses=[self.question['correct_choose'],self.question['wrong_chooses']]
                    random.shuffle(chooses)
                    self.message=[self.question['question'],chooses]
            else:
                self.message=["Sorry i  don't understand you"]
                self.message=random.choice(env.Chat_public_responses["What's your name"])+ random.choice(env.Chat_public_responses["what is your purpose"])
            self.message.append(self.message)
            return self.message
    def Chat_State_One(self,message):
        if self.question != None and self.answer != None:
            if self.Current_State['activity']=='reading':
                if self.Current_State['sub-activtiy']=='reading words':
                    if self.message.__contains__(self.answer[0]):
                        self.Current_State['state']=0
                        self.Profile_history['marks']['0']+=1
                        self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}
                    else:
                        self.message=''
    def Reading_Words(self):
        self.question,self.answer,self.Current_State=self.Reading_Model.Next()
        self.message=[self.question['word'],self.question['description'],self.question['image']]
        
import random
import Chat_Variables as env
import Model_Reading as Reading_Model 
import Model_Writing as Writing_Model
class Chat:
    def __init__(self):
        self.messages=[]
        self.Current_State={'state':0,'activity':'','sub-activity':''}
        self.Profile_history={'username':'','email':'','level':0,'marks':{'0':0,'1':0,'2':0,'3':0,'4':0}}
        self.question=[]
        self.answer=[]
        self.Reading_Model=Reading_Model.Reading_Model(self.Profile_history['level'])
        self.Writing_Model=Writing_Model.Writing_Model(self.Profile_history['level'])
    def respond(self,message):
        # if the state of the chat is zero then it is not waiting a reponse from the user else then the chat is waiting a respo
        if self.Current_State["state"]==0:
            # if the message refers to that the user needs to start learning
            if message in env.User_Public_messages['start laerning']:
                self.messages.append(random.choice(env.Chat_public_messages["let's start learning"]))
                self.question,self.answer,self.Current_State=self.Reading_Model.Next()
                self.messages=[self.question['word'],self.question['description'],self.question['image']]



            # if the user is asking about the chat
            elif message in env.User_Public_messages["what's that"]:
                self.messages=random.choice(env.Chat_public_messages["What's your name"])+ random.choice(env.Chat_public_messages["what is your purpose"])


            # if the user is in reading state
            elif self.Current_State['activity']=='reading':
                self.question,self.answer,self.Current_State=self.Reading_Model.Next()
                if self.Current_State['sub-activity']=='reading words':
                    self.messages=[self.question['word'],self.question['description'],self.question['image']]
                elif self.Current_State['sub-activity']=='choose words':
                    chooses=[self.question['correct_choose'],self.question['wrong_chooses']]
                    random.shuffle(chooses)
                    self.messages=[self.question['question'],chooses]

            else:
                self.messages=["Sorry i  don't understand you"]
                self.messages=random.choice(env.Chat_public_messages["What's your name"])+ random.choice(env.Chat_public_messages["what is your purpose"])
        else:
            if self.question != None and self.answer != None:
                if self.Current_State['activity']=='reading':
                    if self.Current_State['sub-activitiy']=='reading words':
                        if message.__contains__(self.answer[0]):
                            self.Current_State['state']=0
                            self.Profile_history['marks']['0']+=1
                            self.Current_State={'state':0,'activity':'reading','sub-activity':'reading words'}
                        else:
                            self.messages=''
        return self.messages
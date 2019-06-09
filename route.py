from flask import Flask,request, Response
from Chat_Controller.Chat import Chat as chat_model
app = Flask(__name__)
chat=chat_model()
@app.route('/api/v1/chat/',methods=['POST','GET'])
def Getchat():
    response=None
    if request.method=='GET':
        #region User data
        #region User Chat history
        response="GET Method"
    elif request.method=='POST':
        #region Append to chat hist
        #Repond
        response ="POST Method"
    return response
if __name__== "__main__":
    app.run(debug=True)
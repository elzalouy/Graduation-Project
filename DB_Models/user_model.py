import pymongo
import hashlib
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
db=myclient['GPdatabase']
user_model=db["user"]

password='ezat'
hashpass=hashlib.md5(password.encode())

user={
    "username":"ezat elzlouy",
    "email":"ezatelzalouy711@gmail.com",
    "password":hashpass
}


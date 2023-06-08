from pymongo import MongoClient
from flask import Flask,request,abort
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"

client = MongoClient(connection)
app = Flask(__name__)

@app.route('/')
def index():
        try:
                email = str(request.args.get("email"))
        except:
                return "'email' parameter was not specified",404
        email = str(request.args.get("email"))
        #client = MongoClient("mongodb://localhost:27017/")
        database = client["xade"]
        users = database["users"]
        try:
                userDetails = users.find_one({"Email":str(email)})
        except:
                return f"Email Address was not found",404
        userDetails = users.find_one({"Email":str(email)})
        if userDetails == None:
            return "Email Address was not found",404
        uid = userDetails["ID"]
        wallets = database["wallets"]
        try:
                walletDetails = wallets.find_one({"ID":uid})
        except:
                return "Wallet Address was not found",404
        walletDetails = wallets.find_one({"ID":uid})

        return walletDetails["Wallet Address"],200

@app.route('/polygon')
def polygon():
        try:
                email = str(request.args.get("email"))
        except:
                return "'email' parameter was not specified",404
        email = str(request.args.get("email"))
        database = client["mobile"]
        users = database["users"]
        try:
                userDetails = users.find_one({"Email":str(email)})
        except:
                return f"Email Address was not found",404
        userDetails = users.find_one({"Email":str(email)})
        if userDetails == None:
            return "Email Address was not found",404
        address = userDetails["SCW Address"]
        return address,200

@app.route('/polygonlogintype')
def polygonLogintype():
        try:
                email = str(request.args.get("email"))
        except:
                return "'email' parameter was not specified",404
        email = str(request.args.get("email"))
        database = client["mobile"]
        users = database["users"]
        try:
                userDetails = users.find_one({"Email":str(email)})
        except:
                return f"Email Address was not found",404
        return userDetails["Login Type"], 200

if __name__ == '__main__':
        app.run('127.0.0.1',8006)

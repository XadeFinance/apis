from pymongo import MongoClient
from flask import Flask,request,abort
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
app = Flask(__name__)

@app.route('/polygon')
def index():
        try:
                wallet = str(request.args.get("address"))
        except:
                return "'address' parameter was not specified",404
        wallet = str(request.args.get("address"))
        #client = MongoClient("mongodb://localhost:27017/")
        database = client["mobile"]
        wallets = database["wallets"]
        try:
                walletDetails = wallets.find_one({"Wallet Address":str(wallet)})
        except:
                return "wallet address was not found",404
        walletDetails = wallets.find_one({"Wallet Address":str(wallet)})
        if walletDetails == None:
            return "wallet address was not found",404
        uid = walletDetails["ID"]
        users = database["users"]
        try:
                usernameDetails = users.find_one({"ID":uid})
        except:
                return "username was not found",404
        userDetails = users.find_one({"ID":uid})
        return userDetails["Username"],200

@app.route('/uuid')
def uuid():
        try:
                wallet = str(request.args.get("uuid"))
        except:
                return "'uuid' parameter was not specified",404
        uuid = str(request.args.get("uuid"))
        #client = MongoClient("mongodb://localhost:27017/")
        database = client["mobile"]
        wallets = database["wallets"]
        users = database["users"]
        try:
                usernameDetails = users.find_one({"ID":str(uuid)})
        except:
                return "username was not found",404
        userDetails = users.find_one({"ID":uuid})
        return userDetails["Username"],200

if __name__ == '__main__':
        app.run('127.0.0.1',8003)

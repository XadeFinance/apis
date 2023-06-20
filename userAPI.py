from pymongo import MongoClient
from flask import Flask,request,abort
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"

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
        users = database["users"]
        try:
                userDetails = users.find_one({"SCW Address":str(wallet)})
        except:
                return "wallet address was not found",404
        userDetails = users.find_one({"SCW Address":str(wallet)})
        if userDetails == None:
            return "wallet address was not found",404
        return userDetails["Username"],200

@app.route('/uuid')
def uuid():
        try:
                wallet = str(request.args.get("uuid"))
        except:
                return "'uuid' parameter was not specified",404
        uuid = str(request.args.get("uuid"))
        database = client["mobile"]
        wallets = database["wallets"]
        users = database["users"]
        try:
                usernameDetails = users.find_one({"ID":str(uuid)})
        except:
                return "username was not found",404
        userDetails = users.find_one({"ID":uuid})
        return userDetails["SCW Address"],200

@app.route('/email')
def email():
        try:
                address = str(request.args.get("address"))
        except:
                return "'address' parameter was not specified",404
        address = str(request.args.get("address"))
        database = client["mobile"]
        users = database["users"]
        try:
                userDetails = users.find_one({"SCW Address":str(address)})
        except:
                return f"Wallet Address was not found",404
        userDetails = users.find_one({"SCW Address":str(address)})
        if userDetails == None:
            return "Email Address was not found",404
        email = userDetails["Email"]
        return email,200

@app.route('/mercleAPI')
def mercle():
        try:
                address = str(request.args.get("address"))
        except:
                return "'address' parameter was not specified",404
        address = str(request.args.get("address"))
        database = client["mobile"]
        users = database["users"]
        try:
                userDetails = users.find_one({"SCW Address":str(address)})
                return True, 200
        except:
                return False,404

if __name__ == '__main__':
        app.run('127.0.0.1',8003)

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
def polygon():
        try:
                phone = str(request.args.get("phone"))
        except:
                return "'phone' parameter was not specified",404
        phone = str(request.args.get("phone"))
        database = client["mobile"]
        users = database["users"]
        print(phone)
        try:
                userDetails = users.find_one({"Phone": phone})
        except:
                return f"User was not found",404
        userDetails = users.find_one({"Phone": phone})
        print(userDetails)
        if userDetails == None:
            return "Phone Number was not found",404
        address = userDetails["SCW Address"]
        return address,200

if __name__ == '__main__':
        app.run('127.0.0.1',8002)

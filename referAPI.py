from flask import Flask,request,redirect
from os import getenv
from re import match
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
app = Flask(__name__)

@app.route("/<address>")
def redirect(address):
  address = str(address)
  if match("^0x[a-fA-F0-9]{40}$",address):
    return redirect(f"https://shardeum.app.xade.finance/register/{str(address)}")
  else:
    return redirect("https://shardeum.app.xade.finance")
  
@app.route("/api/<address>")
def api(address):
  if match("^0x[a-fA-F0-9]{40}$",address):
    address = str(address).lower()
    database = client["shardeum"]
    users = database["users"]
    referrals = users.find({"Referral":str(address)})
    count = 0
    for ref in referrals:
      count = count+1
    return str(count)
if __name__ == '__main__':
        app.run('127.0.0.1',8005)
      
  
  
  

  
  
  

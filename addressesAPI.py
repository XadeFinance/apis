from flask import Flask, Response
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
db = client["shardeum"]

wallets = db["wallets"]

@app.route(f"/{getenv('emailPass')}", methods=["GET"])
def get_wallets():
    addresses = []
    for wallet in wallets.find({}, {"Wallet Address": 1}):
        addresses.append(wallet["Wallet Address"])
    return Response("\n".join(addresses), mimetype="text/plain")

if __name__ == "__main__":
    app.run('127.0.0.1',8009)

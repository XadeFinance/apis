from flask import Flask, request
from requests import get as rget
from json import loads, dumps
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    try:
            address = str(request.args.get("address"))
    except:
            return "'address' parameter was not specified",404
    address = str(request.args.get("address"))

    txHistory = []

    responseJSON = loads(rget(f"https://explorer-liberty20.shardeum.org/api/transaction?address={address}&txType=4").content)
    txArr = responseJSON["transactions"]
    for tx in txArr:
        if tx["contractInfo"]["name"] == "XadeUSD" and tx["contractInfo"]["symbol"] == "XUSD":
            txHash = tx['txHash']
            timestamp = (datetime.fromtimestamp(tx['timestamp']/1000)).strftime('%B %d %Y, %I:%M %p')
            txFrom = tx['tokenFrom']
            txTo = tx['tokenTo']
            value = int(tx["tokenValue"],16)/ 10 ** 18

            txHistory.append(
                {
                "txHash":txHash,
                "timestamp":timestamp,
                "txFrom":txFrom,
                "txTo":txTo,
                "value":value
                }
                )
    return dumps(txHistory)

if __name__ == '__main__':
    app.run()

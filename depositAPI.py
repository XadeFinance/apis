from flask import Flask,request,abort
from requests import get as rget
from json import loads
app = Flask(__name__)

@app.route("/")
def index():
    try:
            address = str(request.args.get("address"))
    except:
            return "'address' parameter was not specified",404
    address = str(request.args.get("address"))

    url = f"https://explorer-liberty20.shardeum.org/api/transaction?address={address}&txType=4"
    response = rget(url)
    jsonDocs = loads(response.text)["transactions"]
    amtDeposit = 0
    for doc in jsonDocs:
        if doc["tokenTo"] == "0x949b5ff303ea7d3a5a11d7092c9cf2a9b5323fe1":
            amtDeposit = amtDeposit + int(doc["tokenValue"],16)
    if amtDeposit != 0.00:
        amtDeposit = round(amtDeposit/(10**18),2)
    return str(amtDeposit)

if __name__ == '__main__':
      app.run('127.0.0.1',8007,debug=False)

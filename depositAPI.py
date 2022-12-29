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

    url = f"https://api-alfajores.celoscan.io/api?module=account&action=tokentx&contractaddress=0x874069fa1eb16d44d622f2e0ca25eea172369bc1&address={address}"
    response = rget(url)
    jsonDocs = loads(response.text)["result"]
    amtDeposit = 0.00
    for doc in jsonDocs:
        if doc["to"] == "0x7765e4256e0dbda401ce64809bab5aefdca40f08":
            amtDeposit = amtDeposit + float(doc["value"])
    if amtDeposit != 0.00:
        amtDeposit = round(amtDeposit/(10**18),2)
    return str(amtDeposit)

if __name__ == '__main__':
      app.run('127.0.0.1',8007,debug=False)

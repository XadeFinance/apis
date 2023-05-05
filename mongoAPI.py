from flask import Flask, request, redirect
from json import loads
from pymongo import MongoClient
from os import getenv,system
from dotenv import load_dotenv

load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    database = client["xade"]
    users = database["users"]
    wallets = database["wallets"]
    phones = database["phones"]
    if request.method == 'GET':
        return redirect('https://app.xade.finance', code=301)
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        if data.startswith("address:"):
            z = data.split("||")
            adr = z[0].replace("address:","")
            i = z[1].replace("id:","")
            scw = z[2];
            addrChk = wallets.find_one({"Wallet Address":adr})
            if addrChk == None:
                x = wallets.insert_one({"Wallet Address":adr,"ID":i, "scw":scw})

        elif data.startswith('{"phone":'):
            p = loads(data)
            phn = p["phone"]
            i = p["id"]
            phnChk = phones.find_one({"Phone Number":phn})
            if phnChk == None:
                x = phones.insert_one({"Phone Number":phn,"ID":i})

        else:
            j = data.replace("'", "\"")
            d = loads(j)

            email = d["email"]
            name = d["name"]
            pfp = d["profileImage"]
            verify = d["verifier"]
            i = d["verifierId"]
            login = d["typeOfLogin"]
            i = d["id"]
            if login == "jwt":
                login = "email"

            emailAndLoginChk = users.find_one({"Email":email,"Login Type":login})
            if emailAndLoginChk == None:
                info = {
                    "Email":email,
                    "Username":name,
                    "Login Type":login,
                    "ID":i
                }

                x = users.insert_one(info)

            else:
                info = "duplicate lol"

        return data

@app.route('/shardeum', methods=['GET', 'POST'])
def shardeum():
    database = client["shardeum"]
    users = database["users"]
    wallets = database["wallets"]
    phones = database["phones"]
    if request.method == 'GET':
        return redirect('https://app.xade.finance', code=301)
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        if data.startswith("address:"):
            z = data.split("||")
            adr = z[0].replace("address:","")
            i = z[1].replace("id:","")
            addrChk = wallets.find_one({"Wallet Address":adr})
            if addrChk == None:
                x = wallets.insert_one({"Wallet Address":adr,"ID":i})

        elif data.startswith('{"phone":'):
            p = loads(data)
            phn = p["phone"]
            i = p["id"]
            phnChk = phones.find_one({"Phone Number":phn})
            if phnChk == None:
                x = phones.insert_one({"Phone Number":phn,"ID":i})

        else:
            j = data.replace("'", "\"")
            d = loads(j)

            email = d["email"]
            name = d["name"]
            pfp = d["profileImage"]
            verify = d["verifier"]
            i = d["verifierId"]
            login = d["typeOfLogin"]
            i = d["id"]
            if login == "jwt":
                login = "email"

            emailAndLoginChk = users.find_one({"Email":email,"Login Type":login})
            if emailAndLoginChk == None:
                info = {
                    "Email":email,
                    "Username":name,
                    "Login Type":login,
                    "ID":i
                }

                x = users.insert_one(info)

            else:
                info = "duplicate lol"

        return data

@app.route('/polygon', methods=['GET', 'POST'])
def polygon():
    database = client["mobile"]
    users = database["users"]
    wallets = database["wallets"]
    phones = database["phones"]
    if request.method == 'GET':
        return redirect('https://app.xade.finance', code=301)
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        if data.startswith("address:"):
            z = data.split("||")
            adr = z[0].replace("address:","")
            i = z[1].replace("id:","")
            scw = z[2];
            addrChk = wallets.find_one({"Wallet Address":adr})
            if addrChk == None:
                x = wallets.insert_one({"Wallet Address":adr,"ID":i, "SCW Address":scw})
            print(adr)

        elif data.startswith('{"phone":'):
            p = loads(data)
            phn = p["phone"]
            i = p["id"]
            phnChk = phones.find_one({"Phone Number":phn})
            if phnChk == None:
                x = phones.insert_one({"Phone Number":phn,"ID":i})

        else:
            j = data.replace("'", "\"")
            d = loads(j)

            email = d["email"]
            name = d["name"]
            pfp = d["profileImage"]
            verify = d["verifier"]
            i = d["verifierId"]
            login = d["typeOfLogin"]
            i = d["id"]
            if login == "jwt":
                login = "email"

            emailAndLoginChk = users.find_one({"Email":email,"Login Type":login})
            if emailAndLoginChk == None:
                info = {
                    "Email":email,
                    "Username":name,
                    "Login Type":login,
                    "ID":i
                }
                
                v2Db = client["remmitex"]
                testnet = v2Db["testnet"]
                mainnet = v2Db["mainnet"]

                checkTestnet = testnet.find_one({'Email': email})
                if checkTestnet:
                    amount = int(float(checkTestnet.get("Amount")) * pow(10,18))
                    checkAddress = wallets.find_one({'ID':i})
                    if checkAddress:
                        address = checkAddress.get("SCW Address")
                        print(address)
                        print(amount)
                        system(f"node /home/xade/xade-api/testnetV2.js {address} {amount}") 
                        deleteDoc = testnet.delete_one({'Email': email})
                
                checkMainnet = mainnet.find_one({'Email': email})
                if checkMainnet:
                    amount = int(float(checkMainnet.get("Amount")) * pow(10,18))
                    checkAddress = wallets.find_one({'ID':i})
                    if checkAddress:
                        address = checkAddress.get("SCW Address")
                        print(address)
                        print(amount)
                        system(f"node /home/xade/xade-api/mainnetV2.js {address} {amount}")
                        deleteDoc = mainnet.delete_one({'Email': email})

                x = users.insert_one(info)
                
                print(email)
            else:
                info = "duplicate lol"

        return data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

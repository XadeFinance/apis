from flask import Flask, request, redirect
from json import loads
from pymongo import MongoClient
from os import getenv
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
    database = client["mainnet"]
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

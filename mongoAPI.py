from flask import Flask, request, redirect
from json import loads
from pymongo import MongoClient
from os import getenv,system
from dotenv import load_dotenv

load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
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

@app.route('/polygon', methods=['GET', 'POST'])
def polygon():
    database = client["mobile"]
    users = database["users"]
    if request.method == 'GET':
        return redirect('https://app.xade.finance', code=301)
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        if data.startswith("test"):
            return "im up"
        else:
            j = data.replace("'", "\"")
            d = loads(j)

            email = d["email"]
            phone = d["phone"]
            name = d["name"]
            login = d["typeOfLogin"]
            eoa = d["eoa"]
            scw = d["scw"]
            i = d["id"]
            phoneAndLoginChk = None
            emailAndLoginChk = None
            
            if phone == "NULL":
                emailAndLoginChk = users.find_one({"Email":email,"Login Type":login})
                phoneAndLoginChk = None
            else if email == "NULL":
                phoneAndLoginChk = users.find_one({"Phone":phone,"Login Type":login})
                emailAndLoginChk = None
            
            if emailAndLoginChk == None and phoneAndLoginChk == None:
                info = {
                    "Email":email,
                    "Phone":phone,
                    "Username":name,
                    "Login Type":login,
                    "Wallet Address":eoa,
                    "SCW Address":scw,
                    "ID":i
                }
                
                v2Db = client["remmitex"]
                testnet = v2Db["testnet"]
                mainnet = v2Db["mainnet"]

                x = users.insert_one(info)
                address = scw
                
                checkTestnet = testnet.find_one({'Email': email})
                if checkTestnet:
                    amount = int(float(checkTestnet.get("Amount")) * pow(10,18))
                    print(address)
                    print(amount)
                    system(f"node /home/xade/xade-api/testnetV2.js {address} {amount}") 
                    deleteDoc = testnet.delete_one({'Email': email})
                
                checkMainnet = mainnet.find_one({'Email': email})
                if checkMainnet:
                    amount = int(float(checkMainnet.get("Amount")) * pow(10,6))
                    print(address)
                    print(amount)
                    system(f"node /home/xade/xade-api/mainnetV2.js {address} {amount}")
                    deleteDoc = mainnet.delete_one({'Email': email})
                    
                checkTestnet = testnet.find_one({'Phone': phone})
                if checkTestnet:
                    amount = int(float(checkTestnet.get("Amount")) * pow(10,18))
                    print(address)
                    print(amount)
                    system(f"node /home/xade/xade-api/testnetV2.js {address} {amount}") 
                    deleteDoc = testnet.delete_one({'Phone': phone})
                
                checkMainnet = mainnet.find_one({'Phone': phone})
                if checkMainnet:
                    amount = int(float(checkMainnet.get("Amount")) * pow(10,6))
                    print(address)
                    print(amount)
                    system(f"node /home/xade/xade-api/mainnetV2.js {address} {amount}")
                    deleteDoc = mainnet.delete_one({'Phone': phone})
                
                print(email)
                print(phone)
            else:
                info = "duplicate lol"

        return data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

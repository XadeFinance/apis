from flask import Flask,request,abort
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
from requests import get as rget
load_dotenv()
app = Flask(__name__)

password = getenv("emailPass")

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)

database1 = client["shardeum"]
collection = database1["amtOwed"]

@app.route('/')
def index():
  fromAddr = str(request.args.get("from")).lower() 
  toEmail = str(request.args.get("to"))
  amount = float(request.args.get("amt"))
  
  existing_record = collection.find_one({"Email": toEmail})

  if existing_record:
      
      new_amount = existing_record["Amount"] + amount
      collection.update_one({"Email": toEmail}, {"$set": {"Amount": new_amount}})
  else:
      collection.insert_one({"Email": toEmail, "Amount": amount})
  msg = MIMEMultipart()
  msg.set_unixfrom('author')
  msg['From'] = "XADE <development@xade.finance>"
  msg['To'] = f"<{toEmail}>"
  msg['Subject'] = "Payment Received in Xade Account"
  #print("hello1")
  resp = rget(f"https://user.api.xade.finance/shardeum?address={fromAddr}")
  #print("hello2")
  username = ""
  if resp.status_code == 200:
    username = resp.text
  html = f"""
  {username} ({fromAddr[:6] + "..." + fromAddr[-4:]}) has sent ${amount} to your Xade Account
  <br>
  <br>
  Use <a href='https://shardeum.app.xade.finance/register/{fromAddr}'>this link</a> to claim the amount by creating your Xade Account
  <br>
  """
  message = MIMEText(html,'html')
  msg.attach(message)
  mail = smtplib.SMTP_SSL('smtpout.secureserver.net',465)
  mail.ehlo()
  dev = "development@xade.finance"
  mail.login(dev,password)
  mail.sendmail(dev,toEmail,msg.as_string())
  mail.quit()
  return "donezo"
if __name__ == "__main__":
    app.run('127.0.0.1',8010)

#!/usr/bin/env python


import json
import os
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

from flask import Flask
from flask import request
from flask import make_response


# firebase
cred = credentials.Certificate("./ngabantos-database.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://ngabantos-30dc9.firebaseio.com"
})

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])


def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)  
    
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    
    return r




def makeWebhookResult(req):   
    #push user id to firebase
    userid = req.get("originalRequest")
    database = db.reference()
    userp = database.child("user")
    userp.update({
        "name" : userid
    })
    
    if req.get("result").get("action") == "pupuk": 
        database = db.reference()
        pupuk = database.child("Bandung/harga/pupuk")
        jenisp=[]
        hargap=[]
        snapshot = pupuk.order_by_key().get()
        for key, val in snapshot.items():
            jenisp.append(key);
            hargap.append(val);
        
        
        x=0
        hasil=""
        for i in jenisp:
            hasil = hasil + i +" "+hargap[x]+"\n\n"
            x=x+1

        return {
            "speech": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            "displayText": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            #"data": {},
            #"contextOut": [],
            "source": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) "
        }
    
    if req.get("result").get("action") == "bibit": 
        database = db.reference()
        pupuk = database.child("Bandung/harga/bibit")
        jenisp=[]
        hargap=[]
        snapshot = pupuk.order_by_key().get()
        for key, val in snapshot.items():
            jenisp.append(key);
            hargap.append(val);
        
        
        x=0
        hasil=""
        for i in jenisp:
            hasil = hasil + i +" "+hargap[x]+"\n\n"
            x=x+1

        return {
            "speech": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            "displayText": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            #"data": {},
            #"contextOut": [],
            "source": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) "
        }
    
    if req.get("result").get("action") == "peralatan": 
        database = db.reference()
        pupuk = database.child("Bandung/harga/peralatan")
        jenisp=[]
        hargap=[]
        snapshot = pupuk.order_by_key().get()
        for key, val in snapshot.items():
            jenisp.append(key);
            hargap.append(val);
        
        
        x=0
        hasil=""
        for i in jenisp:
            hasil = hasil + i +" "+hargap[x]+"\n\n"
            x=x+1

        return {
            "speech": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            "displayText": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) ",
            #"data": {},
            #"contextOut": [],
            "source": hasil+"\n \n Terima Kasih telah bertanya ke Mila \n :) :) :) "
        }
    
    if req.get("result").get("action") == "saranbener": 
        aa = req.get("result").get("resolvedQuery")
        database = db.reference()
        userp = database.child("Bandung").child("Saran")
        userp.push({
            "Saran" : str(aa)
        })
        return {
            "speech": "\n Terima Kasih telah memberi saran ke Mila \n :) :) :) ",
            "displayText": "\n Terima Kasih telah memberi saran ke Mila \n :) :) :) ",
            #"data": {},
            #"contextOut": [],
            "source": "\n Terima Kasih telah memberi saran ke Mila \n :) :) :) " 
        }
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')

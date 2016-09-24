"""
Routes and views for the flask application.
"""
import datetime
from flask import render_template
from RiseAPIs import app
import requests
import urllib2
import json
import time

@app.route('/test')
def api1():
    numdays = 3
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
    data = list()
    for value in date_list:
        #response = requests.get("http://api.fixer.io/"+str(value)+"?base=GBP&symbols=USD,INR,EUR")
        #data.append(response.text)
        #time.sleep(1)
        print value
    return data
@app.route('/')
def api():
    #Output
    json_output = dict()

    #Currency Exchange
    barclays_ipr = "http://api119105sandbox.gateway.akana.com:80/fxRates"
    #response = requests.get("http://api.fixer.io/latest?base=GBP&symbols=USD,INR,EUR")
    #response.close()
    #currencyData = json.JSONDecoder(response.text)
    currencyData = "{\"base\":\"GBP\",\"date\":\"2016-09-24\",\"rates\":{\"INR\":86.436,\"USD\":1.2974,\"EUR\":1.1569}}"
    json_output["currency"]=json.loads(currencyData)

    #Currency Trend
    last_month = requests.get("http://api.fixer.io/2015-09-24?base=GBP&symbols=USD")
    currencyData_last = json.JSONDecoder(last_month.text)
    #last_month.close()
    #latest = requests.get("http://api.fixer.io/latest?base=GBP&symbols=USD")
    #currencyData_current = json.JSONDecoder(latest.text)
    #latest.close()
    #if(float(currencyData_current[2]["USD"]) < float(currencyData_last[2]["USD"])):
    #    json_output["market_sentiment"]=True
    #else:
    #    json_output["market_sentiment"]=False
    json_output["market_sentiment"]=False
    return(json.JSONEncoder().encode(json_output))
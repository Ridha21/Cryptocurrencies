import requests

pi='4976d29d2ffb43259ac94f12ff54646d'

def conversion():
    
    '''Currency Conversion '''

url = 'http://api.coinlayer.com/convert? access_key = 4976d29d2ffb43259ac94f12ff54646d & from = BTC& to = USD& amount = 10'
params = {'access_key': api, 'from': 'BTC','to':'USD', 'amount': 20}
r = requests.get('http://api.coinlayer.com/convert', params = params)
convcoin = r.json()
print (convcoin)

def hist():
    
    '''Fetch Historical Data'''
  
url = 'http://api.coinlayer.com/2019-04-30? access_key = 4976d29d2ffb43259ac94f12ff54646d '
params = {'access_key': api, 'date': '2019-04-30','currencies': 'USD,EUR,CNY,HKD', 'expand': 1}
r = requests.get('http://api.coinlayer.com/2018-04-30', params = params)
convcoin = r.json()
print (convcoin)

def timeframe():
    
    '''Fetch Data in a specific timeframe'''

url = 'http://api.coinlayer.com/timeframe? access_key = 4976d29d2ffb43259ac94f12ff54646d & start_date = 2018-04-01& end_date = 2018-04-30& symbols = BTC,ETH '
params = {'access_key': api, 'start_date': '2018-04-01','end_date': '2018-04-30','currencies': 'BTC,ETH', 'expand': 1}
r = requests.get('http://api.coinlayer.com/2018-04-30', params = params)
convcoin = r.json()
print (convcoin)

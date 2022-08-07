import requests
headers = {
        'X-CMC_PRO_API_KEY': 'your_api_key',
        'Accepts': 'application/json'
    }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

def getTop(posicion):
    params = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }
    json = requests.get(url, params = params, headers = headers).json()
    coins =  json['data']
    return coins[posicion]['name']

def iniciarDiccionario(clave):
    params = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    json = requests.get(url, params = params, headers = headers).json()
    coins =  json['data']
    for coin in coins:
        if coin['name'] == clave or coin['symbol'] == clave:
            INFO = { "nombre": coin['name'], "symbol" : coin['symbol'], "circSupply" : round(coin['circulating_supply'],5), "price":round(coin['quote']['USD']['price'],5), "marketCap":round(coin['quote']['USD']['market_cap'],5)}
    return INFO
import requests

def wallets(coin):
    if (coin == 'doge'):
        return ''
    elif (coin == 'ltc'):
        return ''

def get_balance(coin):

    global wallets

    balance = requests.get('https://block.io/api/v2/get_address_balance/?api_key=api-key&addresses='+wallets(coin)).json()

    return balance['data']['balances'][0]['available_balance']
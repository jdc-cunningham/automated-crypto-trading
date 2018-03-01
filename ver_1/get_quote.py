import requests

def get_quote(pair,amount):
    
    global requests

    quote_req = requests.post('https://shapeshift.io/sendamount', data = {
        'amount':amount,
        'pair':pair
    })

    return quote_req.json()
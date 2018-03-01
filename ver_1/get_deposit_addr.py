import requests

# block io address
ltc_addr = ''
doge_addr = ''

def get_deposit_addr(amount,pair,withdrawal_addr):

    print withdrawal_addr

    global requests

    def get_return_addr(pair):

        from_coin = pair.split('_')[0]

        if ('ltc' in from_coin):
            return ltc_addr
        elif ('doge' in from_coin):
            return doge_addr

    tx_req = requests.post('https://shapeshift.io/sendamount', data = {
        'amount': amount,
        'withdrawal': withdrawal_addr,
        'pair': pair,
        'returnAddress': get_return_addr(pair)
    })

    return tx_req.json()
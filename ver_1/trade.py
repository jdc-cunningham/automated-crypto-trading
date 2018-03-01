# dependencies
import requests
from get_quote import get_quote
from get_balance import get_balance
from get_deposit_addr import get_deposit_addr

# trade function

# global variables
# block.IO
ltc_wallet_addr = ''
# coinomi
doge_wallet_addr = ''
digibyte_wallet_addr = ''
lbry_credits_wallet_addr = ''
potcoin_wallet_addr = ''
reddcoin_wallet_addr = ''
voxels_wallet_addr = ''
vericoin_wallet_addr = ''

# return wallet addr functions
def ltc():
    return ltc_wallet_addr
def doge():
    return doge_wallet_addr

def digi_byte():
    return digibyte_wallet_addr

def lbry_credits():
    return lbry_credits_wallet_addr

def potcoin():
    return potcoin_wallet_addr

def reddcoin():
    return reddcoin_wallet_addr

def voxels():
    return voxels_wallet_addr

def vericoin():
    return vericoin_wallet_addr

deposit_addr_lookup = {
    'ltc': ltc,
    'doge': doge,
    'dgb': digi_byte,
    'lbc': lbry_credits,
    'pot': potcoin,
    'rdd': reddcoin,
    'vox': voxels,
    'vrc': vericoin
}

coin_addr = {
    'doge': doge,
    'dgb': digi_byte,
    'lbc': lbry_credits,
    'pot': potcoin,
    'rdd': reddcoin,
    'vox': voxels,
    'vrc': vericoin
}

coin_symbol = {
    'ltc': 'ltc',
    'doge': 'doge',
    'digibyte': 'dgb',
    'lbry_credits':'lbc',
    'potcoin': 'pot',
    'reddcoin': 'rdd',
    'voxels': 'vox',
    'vericoin': 'vrc'
}

def coin_addr_lookup(coin):
    return coin_addr[coin]()


def trade (amount,from_coin,to_coin):
    
    global desposit_addr_lookup

    # pair
    pair = from_coin + '_' + to_coin
    # get quote
    quote = get_quote(pair,amount)
    # check balance
    if ((quote['success']['depositAmount'] + quote['success']['minerFee']) < get_balance('ltc')):
        # can afford
        # make exchange
        deposit_req = get_deposit_addr(amount,pair,deposit_addr_lookup[to_coin]())
        print deposit_req
        deposit_addr = deposit_req['success']['deposit']
        deposit_amount = deposit_req['success']['depositAmount']
        # deposit
        make_deposit = requests.get('https://block.io/api/v2/withdraw/?api_key=api-key&amounts=' + deposit_amount + '&to_addresses=' + deposit_addr + '&pin=secret-pin').json()
        print make_deposit['status']
    else:
        print ("can't afford trade: " + str(amount) + " " + pair)

trade(20,'ltc',coin_symbol['digibyte'])
#!/usr/bin/python

# import websocket
from websocket import create_connection
import json
import pickle
import ast
import time

ws = create_connection("wss://ws-feed.pro.coinbase.com")

ws_sub_obj = {}
ws_sub_obj["type"] = "subscribe"
ws_sub_obj["product_ids"] = ["BTC-USD"]
ws_sub_obj["channels"] = ["ticker"]

# what_is = pickle.load(ws_sub_obj)

print "Subscribe to BTC-USD"
ws.send(
    # what_is
    json.dumps(ws_sub_obj)
    # {
    #     "type": "subscribe",
    #     "product_ids": [
    #         "ETH-USD",
    #         "ETH-EUR"
    #     ],
    #     "channels": [
    #         "level2",
    #         "heartbeat",
    #         {
    #             "name": "ticker",
    #             "product_ids": [
    #                 "ETH-BTC",
    #                 "ETH-USD"
    #             ]
    #         }
    #     ]
    # }
)
# print "Sent"
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result

while True:
    time.sleep(0.1)
    result = ws.recv()
    # print json.loads(result).price
    ticker_obj = json.loads(result)
    if 'channels' not in result:
        print ticker_obj['price']

# def output():
#     print "Received '%s'" % result

# while True:
# ws.onmessage() = output
# ws.close()
